from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from helper import login_required, encryption, decryption


views = Blueprint("views", __name__)


@views.route("/")
@login_required
def index():
    passwords = db.execute("SELECT id, name, username, email, password, timestamp FROM secrets WHERE user_id = ? ORDER BY timestamp DESC", session["user_id"])
    
    return render_template("index.html", passwords=passwords)


@views.route("/add-item", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("add-username")
        email = request.form.get("email")
        password = request.form.get("add-password")

        check = 0
        for i in db.execute("SELECT name FROM secrets WHERE user_id = ? AND name = ?", session["user_id"], name):
            if name == i["name"]:
                check = 1

        if check == 1:
            flash("Name already inside in the table.", "error")
        else:
            
            passwordEncrypted = encryption(password)

            db.execute("INSERT INTO secrets (name, username, email, password, timestamp, user_id) VALUES (?, ?, ?, ?, datetime('now'), ?)", name, username, email, passwordEncrypted, session["user_id"])

            flash("Item added Successfully.")

            return redirect(url_for("views.index"))

    return redirect(url_for("views.index"))


@views.route("/update-item/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        encryptedPassword = encryption(password)

        db.execute("UPDATE secrets SET name = ?, username = ?, email = ?, password = ?, timestamp = datetime('now') WHERE id = ? AND user_id = ?", name, username, email, encryptedPassword, id, session["user_id"])

        flash("Item Updated Successfully")

        return redirect(url_for("views.index"))

    secrets = db.execute("SELECT name, username, email, password, timestamp FROM secrets WHERE id=?", id)

    decryptedPassword = decryption(secrets[0]["password"]).decode()

    return render_template("update.html", secrets=secrets, decryptedPassword=decryptedPassword)


@views.route("/vault-item/<int:id>", methods=["GET", "POST"])
@login_required
def secret(id):
    secrets = db.execute("SELECT id, name, username, email, password, timestamp FROM secrets WHERE id=?", id)

    try:
        decryptedPassword = decryption(secrets[0]["password"]).decode()
    except IndexError:
        return redirect(url_for("views.index"))

    return render_template('secret.html', secrets=secrets, decryptedPassword=decryptedPassword)


@views.route("/delete/<int:id>", methods=["GET", "POST"])
@login_required
def delete(id):

    if request.method == "POST":
        db.execute("DELETE FROM secrets WHERE id=? AND user_id=?", id, session["user_id"])

        return redirect(url_for("views.index"))
    
    return None


@views.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    informationCurrentUser = db.execute("SELECT id, username, password FROM users WHERE id = ?", session["user_id"])

    decryptedPassword = decryption(informationCurrentUser[0]["password"]).decode()

    return render_template("profile.html", informationCurrentUser=informationCurrentUser, decryptedPassword=decryptedPassword)


@views.route("/update-profile", methods=["GET", "POST"])
@login_required
def updateProfile():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        checkUsername = {}
        for i in db.execute("SELECT id, username FROM users WHERE username = ?", username):
            checkUsername["id"] = i["id"]
            checkUsername["username"] = i["username"]

        try: 
            if checkUsername["id"] != session["user_id"]:  
                flash("Username already taken.", "error")
        except KeyError:
            pass

        if len(password) < 8:
            flash("Password must be greater than 7 characters long.", "error")
        elif password != confirm:
            flash("Passwords doesn't match.", "error")
        else:
            encryptedPassword = encryption(password)

            db.execute("UPDATE users SET username = ?, password = ? WHERE id = ?", username, encryptedPassword, session["user_id"])

            flash("User Updated Successfully")

            return redirect(url_for('views.profile'))

    informationCurrentUser = db.execute("SELECT username, password FROM users WHERE id = ?", session["user_id"])

    decryptedPassword = decryption(informationCurrentUser[0]["password"]).decode()

    return render_template("update-profile.html", informationCurrentUser=informationCurrentUser, decryptedPassword=decryptedPassword)


@views.route("/delete-user/<int:id>", methods=["GET", "POST"])
@login_required
def deleteUser(id):
    
    if request.method == "POST":
        db.execute("DELETE FROM users WHERE id = ?", id)
        db.execute("DELETE FROM secrets WHERE user_id = ?", id)

        return redirect(url_for("auth.login"))

    return None


@views.route("/search", methods=["GET", "POST"])
@login_required
def search():

    if request.method == "POST":
        nameSite = request.form.get("search")

        itemSearched = db.execute("SELECT * FROM secrets WHERE user_id = ? AND name = ? OR email = ?", session["user_id"], nameSite, nameSite)

        if itemSearched == []:
            flash("No items were found that match your search pattern", "error")

            return redirect(url_for("views.index"))

        return render_template("searched.html", itemSearched=itemSearched, nameSite=nameSite)

    return None
