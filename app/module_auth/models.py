from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
from app.module_base.models import Base


class User(UserMixin, Base):
    __tablename__ = 'USER'

    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.SmallInteger, nullable=True)
    status = db.Column(db.SmallInteger, nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    is_supervisor = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
