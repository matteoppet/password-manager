from flask import Flask, render_template, redirect, url_for
from cs50 import SQL

app = Flask(__name__)
app.config['SECRET_KEY'] = '234/423/3wsd9/214asd/2asdj3w2'
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL('sqlite:///database.db')

from auth import auth

app.register_blueprint(auth, url_prefix="/")

@app.route("/")
def index():
    return render_template("index.html")