from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, SubmitField, FloatField, IntegerField, TextAreaField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from app.module_auth.models import User
from app.module_task.models import Task


def user_choice():
    return User.query


def task_choice():
    return Task.query


class TaskForm(FlaskForm):
    task_code = StringField('Ma cong viec', validators=[DataRequired()])
    task_name = StringField('Ten cong viec', validators=[DataRequired()])
    # task_type = StringField('Loai cong viec', validators=[DataRequired()])
    task_type = SelectField('Loai cong viec',
                            choices=[('B', 'Bug'), ('U', 'Usage'), ('TB', 'Testing Bug'), ('MOD', 'Modification'),
                                     ('FT', 'Feature'), ('TS', 'Training/Support'), ('O', 'Others')])
    man_days_quoted = FloatField('Thoi gian lam du kien', default=0)
    man_days_dev = FloatField('Thoi gian lam thuc te', default=0)
    main_sa = StringField('Nguoi chiu trach nhiem', validators=[DataRequired()])
    status = StringField('Trang thai cong viec', validators=[DataRequired()])
    assigned_by = StringField('Nguoi giao cong viec', validators=[DataRequired()])
    assigned_date = DateField('Ngay giao cong viec', default=datetime.utcnow(), format="%Y-%m-%d")
    dev_code = QuerySelectField(label='Nguoi thuc hien', query_factory=user_choice, get_label='username')
    est_start_date_dev = DateField('Ngay du kien bat dau', format="%Y-%m-%d")
    est_end_date_dev = DateField('Ngay du kien hoan thanh', format="%Y-%m-%d")
    qa_code = StringField('Nguoi kiem tra')
    est_start_date_qa = DateField('Ngay du kien bat dau', format="%Y-%m-%d")
    est_end_date_qa = DateField('Ngay du kien hoan thanh', format="%Y-%m-%d")
    description = TextAreaField('Mo ta')
    parent_task_id = QuerySelectField(label='Cong viec lien quan', query_factory=task_choice, get_label='task_name')
    project_id = IntegerField('Project Id')
    priority = IntegerField('Muc do', default=0)
    submit = SubmitField('Submit')
