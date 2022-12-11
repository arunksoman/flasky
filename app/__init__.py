from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import ret_config, env_name
from .model import db

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    config_obj = ret_config(env_name)
    app.config.from_object(config_obj)
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    from .users.user import user_bp as user

    app.register_blueprint(user)
    return app
