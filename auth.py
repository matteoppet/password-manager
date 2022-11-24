from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from app import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("login-password")
        keepLogged = request.form.get("checkbox")

        search_user = db.execute("SELECT id, username, hash FROM users WHERE username = ?", username)

        if len(search_user) != 1 or not check_password_hash(search_user[0]["hash"], password):
            flash("Username or Password incorrect.", "error")
        else:
            session["user_id"] = search_user[0]["id"]

            return redirect("/")

    return render_template('auth/login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("register-password")
        confirm = request.form.get("confirm")

        check = 0
        for i in db.execute("SELECT username FROM users WHERE username = ?", username):
            if username == i["username"]:
                check = 1

        if check == 1:
            flash("Username already taken.", "error")
        elif len(password) < 8:
            flash("Password must be greater than 7 characters long.", "error")
        elif password != confirm:
            flash("Passwords doesn't match.", "error")
        else:
            hash = generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

            flash("Account Created Successfully.")

        return redirect(url_for("auth.login"))
    
    return None

@auth.route("/logout")
def logout():

    session.clear()

    return redirect("auth.login")