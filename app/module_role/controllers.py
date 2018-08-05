from flask import Blueprint, request, render_template, flash, g, sessions, redirect, url_for
from flask_login import login_required
from werkzeug.urls import url_parse
from app import db
from app.module_role.forms import RoleForm, UserRoleForm
from app.module_base.controllers import check_admin
from app.module_role.models import Role, UserRole

module_role = Blueprint('role', __name__, url_prefix='/role')
module_userrole = Blueprint('userrole', __name__, url_prefix='/user_role')


@module_role.route('/', methods=['GET'])
@login_required
def index():
    role_list = Role.query.all()

    return render_template('module_role/index.html', title='Role', role_list=role_list)


@module_role.route('/create/', methods=['GET', 'POST'])
def create():
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(
            role_code=form.role_code.data,
            role_name=form.role_name.data,
            is_supervisor=form.is_supervisor.data
        )

        try:
            db.session.add(role)
            db.session.commit()
            flash('Add Role success')
        except:
            flash('Error when add Role')

        return redirect(url_for('role.index'))
    return render_template('module_role/role.html', title='Role | Create New Role',
                           add_role=add_role, form=form)


@module_role.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    check_admin()
    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=Role)
    if form.validate_on_submit():
        role.role_name = form.role_name.data
        role.is_supervisor = form.is_supervisor.data

        db.session.commit()
        flash('Edit Role success')
        return redirect(url_for('role.index'))

    form.role_name.data = role.role_name
    form.is_supervisor.data = Role.is_supervisor

    return render_template('module_role/role.html', title='Role | Edit Role',
                           add_role=add_role, form=form, role=role)


@module_role.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    check_admin()
    role = Role.query.get_or_404(id)
    role.is_active = False

    db.session.commit()
    flash('Delete successs')

    return redirect(url_for('role.index'))


@module_userrole.route('/', methods=['GET'])
@login_required
def index_user_role():
    user_role_list = UserRole.query.all()

    return render_template('module_role/index_user_role.html', title='Assign User Role', user_role_list=user_role_list)


@module_userrole.route('/create/', methods=['GET', 'POST'])
def create_user_role():
    check_admin()

    add_user_role = True

    form = UserRoleForm()
    if form.validate_on_submit():
        user_role = UserRole(
            role_code=form.role_code.data.role_code,
            username=form.username.data.username
        )

        try:
            db.session.add(user_role)
            db.session.commit()
            flash('Add User Role success')
        except Exception as e:
            flash('Error when add User Role')

        return redirect(url_for('userrole.index_user_role'))
    return render_template('module_role/user_role.html', title='User Role | Create New User Role',
                           add_user_role=add_user_role, form=form)


@module_userrole.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user_role(id):
    check_admin()
    add_user_role = False

    user_role = UserRole.query.get_or_404(id)
    form = UserRoleForm(obj=user_role)
    if form.validate_on_submit():
        user_role.role_code = form.role_code.data
        user_role.username = form.username.data

        db.session.commit()
        flash('Edit User Role success')
        return redirect(url_for('userrole.index_user_role'))

    form.role_code.data = user_role.role_code
    form.username.data = user_role.username

    return render_template('module_role/user_role.html', title='User Role | Edit User Role',
                           add_user_role=add_user_role, form=form, user_role=user_role)


@module_userrole.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_user_role(id):
    check_admin()
    user_role = UserRole.query.get_or_404(id)
    user_role.is_active = False

    db.session.commit()
    flash('Delete successs')

    return redirect(url_for('userrole.index_user_role'))
