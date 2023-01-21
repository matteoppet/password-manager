from flask import Flask, render_template
from cs50 import SQL
from flask_session import Session

from datetime import timedelta


db = SQL('sqlite:///database.db')


def create_app():
    # Setup Flask App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "234/423/3wsd9/214asd/2asdj3w2"

    app.config["TEMPLATES_AUTO_RELOAD"] = True

    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
    Session(app) 


    # Registration of Blueprint
    from auth import auth
    from views import views

    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")


    @app.errorhandler(404)
    def not_found(e):
        return render_template("errors/404.html")

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("errors/500.html")

    return app


if __name__ == '__main__':
    create_app().run()