from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from helper import login_required


views = Blueprint("views", __name__)


@views.route("/")
@login_required
def index():
    return render_template("index.html")
