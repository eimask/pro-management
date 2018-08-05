from datetime import datetime
from app import db
from app.module_base.models import Base


class Role(Base):
    __tablename__ = 'ROLE'

    role_code = db.Column(db.String(50), nullable=False, unique=True)
    role_name = db.Column(db.String(255), nullable=False)
    is_supervisor = db.Column(db.Boolean, default=False)

    # def __init__(self, role_code, role_name, is_supervisor):
    #     self.role_code = role_code
    #     self.role_name = role_name
    #     self.is_supervisor = is_supervisor

    def __repr__(self):
        return '<Role {}>'.format(self.role_code)


class UserRole(Base):
    __tablename__ = 'USER_ROLE'

    role_code = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(128), nullable=False)

    # def __init__(self, role_code, username):
    #     self.role_code = role_code
    #     self.username = username

    def __repr__(self):
        return '<UserRole {}>'.format(self.id)
