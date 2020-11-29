from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from sqlalchemy import text, create_engine

engine = create_engine('oracle://flasky:flasky@127.0.0.1:1521/xe')

db = SQLAlchemy()
bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    
    # blueprint untuk main app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # blueprint untuk auth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    return app