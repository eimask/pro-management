from flask_login import UserMixin
from app import db
from app.module_base.models import Base


class Employee(UserMixin, Base):
    __tablename__ = 'EMPLOYEE'

    employee_code = db.Column(db.String(50), nullable=False)
    employee_name = db.Column(db.String(225))
    employee_short_name = db.Column(db.String(50))
    employee_class_code = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    gender = db.Column(db.SmallInteger, default=0)
    marital_status = db.Column(db.SmallInteger, default=0)
    date_of_birth = db.Column(db.DateTime)
    email_address = db.Column(db.String(225))
    address = db.Column(db.String(225))
    mobile_phone_no = db.Column(db.String(20))
    employment_status = db.Column(db.String(3), default="A")
    join_date = db.Column(db.Date)
    resignation_date = db.Column(db.Date)
    remarks = db.Column(db.String(225))

    def __repr__(self):
        return '<Employee {}>'.format(self.employee_code)
