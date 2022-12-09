from flask import Flask, render_template, redirect, session
from cs50 import SQL
from flask_session import Session

from cryptography.fernet import Fernet

from datetime import timedelta


# Setup Flask App
app = Flask(__name__)
app.config['SECRET_KEY'] = '234/423/3wsd9/214asd/2asdj3w2'

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
Session(app) 


db = SQL('sqlite:///database.db')


# Registration of Blueprint
from auth import auth
from views import views

app.register_blueprint(auth, url_prefix="/")
app.register_blueprint(views, url_prefix="/")


# Instances for cryptography library.
key = Fernet.generate_key()
fernet = Fernet(key)


if __name__ == '__main__':
    app.run(debug=True)