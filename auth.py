from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from helper import login_required, encryption, decryption


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("login-password")
        keepLogged = request.form.get("checkbox")

        searchUser = db.execute("SELECT id, password FROM users WHERE username = ?", username)

        encryptedPassword = None
        for i in searchUser:
            encryptedPassword = i['password']
            id = i["id"]


        if encryptedPassword != None:
            decryptedPassword = decryption(encryptedPassword).decode()


        if len(searchUser) != 1 or password != decryptedPassword:
            flash("Username or Password incorrect.", "error")
        else:
            session["user_id"] = id

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

            encryptedPassword = encryption(password)

            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", username, encryptedPassword)

            flash("Account Created Successfully.")

            return redirect(url_for('auth.login'))
        
        return redirect(url_for('auth.login'))
    
    return None


@auth.route("/logout")
@login_required
def logout():

    session.clear()

    return redirect(url_for("auth.login"))

    