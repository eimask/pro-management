from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from datetime import datetime
from wtforms import StringField, BooleanField, SubmitField, FloatField, DateTimeField, IntegerField, SelectField
from wtforms.validators import DataRequired
from app.module_role.models import Role
from app.module_auth.models import User


class RoleForm(FlaskForm):
    role_code = StringField('Role Code', validators=[DataRequired()])
    role_name = StringField('Role name', validators=[DataRequired()])
    is_supervisor = BooleanField('Is Supervior?', default=False)
    submit = SubmitField('Submit')


def role_choice():
    return Role.query


def user_choice():
    return User.query


class UserRoleForm(FlaskForm):
    # role_code = SelectField(label='Role code', coerce=int, choices=[(tc.id, tc.role_code) for tc in Role.query.order_by('id')])
    # username = SelectField(label='User name', coerce=int, choices=[(tc.id, tc.username) for tc in User.query.order_by('id')])
    role_code = QuerySelectField(query_factory=role_choice, get_pk=lambda a: a.id, get_label=lambda a: a.role_code)
    username = QuerySelectField(query_factory=user_choice, get_pk=lambda a: a.id, get_label=lambda a: a.username)
    submit = SubmitField('Submit')
