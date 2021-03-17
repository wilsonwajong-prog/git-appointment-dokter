from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
login_manger = LoginManager()
db = SQLAlchemy()
login_manger.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hard to guess string'
    app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///data.sqlite'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    bootstrap.init_app(app)
    db.init_app(app)
    login_manger.init_app(app)
    from .main import main as main_blueprinth
    app.register_blueprint(main_blueprinth)
    from .auth import auth as auth_blueprinth
    app.register_blueprint(auth_blueprinth, url_prefix='/auth')
    return app

