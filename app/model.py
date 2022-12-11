from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .users.models import User
