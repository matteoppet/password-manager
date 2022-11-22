from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")

        print("Login Function: " + username)

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