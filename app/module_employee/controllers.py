from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from flask_login import login_required
from werkzeug.urls import url_parse
from app import db, socketio
from app import events
from app.module_employee.forms import EmployeeListForm
from app.module_base.controllers import check_admin
from app.module_employee.models import Employee

module_employee = Blueprint('employee', __name__, url_prefix='/employee')


@module_employee.route('/', methods=['GET'])
@login_required
def index():
    task_list = Task.query.all()

    return render_template('module_task/index.html', title='Task', task_list=task_list)


@module_employee.route('/create/', methods=['GET', 'POST'])
def create():
    check_admin()

    add_task = True

    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            task_code=form.task_code.data,
            task_name=form.task_name.data,
            task_type=form.task_type.data,
            man_days_quoted=form.man_days_quoted.data,
            man_days_dev=form.man_days_dev.data,
            main_sa=form.main_sa.data,
            status=form.status.data,
            assigned_by=form.assigned_by.data,
            assigned_date=form.assigned_date.data,
            dev_code=form.dev_code.data,
            est_start_date_dev=form.est_start_date_dev.data,
            est_end_date_dev=form.est_end_date_dev.data,
            qa_code=form.qa_code.data.id,
            est_start_date_qa=form.est_start_date_qa.data,
            est_end_date_qa=form.est_end_date_qa.data,
            description=form.description.data,
            parent_task_id=form.parent_task_id.data.id,
            project_id=form.project_id.data,
            priority=form.priority.data
        )

        try:
            db.session.add(task)
            db.session.commit()
            flash('Add Task success')
        except Exception as e:
            print(e)
            flash('Error when add task')

        return redirect(url_for('task.index'))
    return render_template('module_task/task.html', title='Task | Create New Task',
                           add_task=add_task, form=form)


@module_employee.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    check_admin()
    add_task = False

    task = Task.query.get_or_404(id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.task_name = form.task_name.data
        task.task_type = form.task_type.data
        task.man_days_quoted = form.man_days_quoted.data
        task.man_days_dev = form.man_days_dev.data
        task.main_sa = form.main_sa.data
        task.status = form.status.data
        task.assigned_by = form.assigned_by.data
        task.assigned_date = form.assigned_date.data
        task.dev_code = form.dev_code.data.id
        task.est_start_date_dev = form.est_start_date_dev.data
        task.est_end_date_dev = form.est_end_date_dev.data
        task.qa_code = form.qa_code.data
        task.est_start_date_qa = form.est_start_date_qa.data
        task.est_end_date_qa = form.est_end_date_qa.data
        task.description = form.description.data
        task.priority = form.priority.data
        task.parent_task_id = form.parent_task_id.data.id
        task.project_id = form.project_id.data

        db.session.commit()
        socketio.emit('message', {'msg': session.get('username') + ':' + 'ok'}, room=form.dev_code.data.username)
        flash('Edit task success')
        return redirect(url_for('task.index'))

    form.task_name.data = task.task_name
    form.task_type.data = task.task_type
    form.man_days_quoted.data = task.man_days_quoted
    form.man_days_dev.data = task.man_days_dev
    form.main_sa.data = task.main_sa
    form.status.data = task.status
    form.assigned_by.data = task.assigned_by
    form.assigned_date.data = task.assigned_date
    form.dev_code.data = task.dev_code
    form.est_start_date_dev.data = task.est_start_date_dev
    form.est_end_date_dev.data = task.est_end_date_dev
    form.qa_code.data = task.qa_code
    form.est_start_date_qa.data = task.est_start_date_qa
    form.est_end_date_qa.data = task.est_end_date_qa
    form.description.data = task.description
    form.priority.data = task.priority
    form.parent_task_id.data = task.parent_task_id
    form.project_id.data = task.project_id

    return render_template('module_task/task.html', title='Task | Edit Task',
                           add_task=add_task, form=form, task=task)


@module_employee.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    check_admin()
    task = Task.query.get_or_404(id)
    task.is_active = False

    db.session.commit()
    flash('Delete successs')

    return redirect(url_for('task.index'))

