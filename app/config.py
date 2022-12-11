from os import path, environ
from enum import Enum
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

env_name = environ.get("ENV")


class Config:
    """
    Commonly used configurations can go here
    """

    FLASK_DEBUG = False
    DEBUG = False
    SECRET_KEY = environ.get("SECRET_KEY")
    SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME")


class ProductionConfig(Config):
    """Production Configuration"""

    FLASK_DEBUG = False
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get("PROD_SQLALCHEMY_DATABASE_URI")


class DevelopmentConfig(Config):
    """Development Configurations"""

    FLASK_DEBUG = True
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_SQLALCHEMY_DATABASE_URI")


class TestingConfig(Config):
    """Testing Configurations"""

    FLASK_DEBUG = True
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get("TEST_SQLALCHEMY_DATABASE_URI")


def ret_config(config_name):
    config_obj_dict = {
        "production": ProductionConfig,
        "development": DevelopmentConfig,
        "testing": TestingConfig,
    }
    return config_obj_dict[config_name]
