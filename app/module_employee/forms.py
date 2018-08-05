from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from app.module_employee.models import Employee


class EmployeeListForm(FlaskForm):
    employee_code = StringField('Employee Code')
    employee_name = StringField('Employee Name')
