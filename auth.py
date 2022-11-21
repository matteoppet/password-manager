from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/registration.html')