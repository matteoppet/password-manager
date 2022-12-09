from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from app import db
from helper import login_required


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
            db.execute("INSERT INTO secrets (name, username, email, password, timestamp, user_id) VALUES (?, ?, ?, ?, datetime('now'), ?)", name, username, email, password, session["user_id"])

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

        db.execute("UPDATE secrets SET name = ?, username = ?, email = ?, password = ?, timestamp = datetime('now') WHERE id = ? AND user_id = ?", name, username, email, password, id, session["user_id"])

        flash("Item Updated Successfully")

        return redirect(url_for("views.index"))

    secrets = db.execute("SELECT name, username, email, password, timestamp FROM secrets WHERE id=?", id)

    return render_template("update.html", secrets=secrets)


@views.route("/vault-item/<int:id>", methods=["GET", "POST"])
@login_required
def secret(id):
    secrets = db.execute("SELECT id, name, username, email, password, timestamp FROM secrets WHERE id=?", id)

    return render_template('secret.html', secrets=secrets)


@views.route("/delete/<int:id>", methods=["GET", "POST"])
@login_required
def delete(id):

    if request.method == "POST":
        db.execute("DELETE FROM secrets WHERE id=? AND user_id=?", id, session["user_id"])

        return redirect(url_for("views.index"))
    
    return None


@views.route("/profile", methods=["GET", "POST"])
def profile():

    if request.method == "POST":
        pass

    informationCurrentUser = db.execute("SELECT username, hash FROM users WHERE id = ?", session["user_id"])

    return render_template("profile.html")