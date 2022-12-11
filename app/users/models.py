from app.model import db
from datetime import datetime

# Refer https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-camelcase-types


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.String(40), unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_deleted = db.Column(db.DateTime, nullable=True)

    def upsert(self):
        db.session.add(self)
        db.session.commit()
