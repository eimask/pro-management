from datetime import datetime
from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    created_by = db.Column(db.Integer, default=-1)
    modified_date = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    modified_by = db.Column(db.Integer, default=-1)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
