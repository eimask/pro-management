from flask import Blueprint, request, render_template, flash, g, redirect, url_for, session
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from app import db
from app.module_auth.forms import LoginForm, RegistrationForm
from app.module_auth.models import User


module_auth = Blueprint('auth', __name__, url_prefix='/auth')


@module_auth.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        curr_user = User.query.filter_by(id=session['userid']).first()
        session['username'] = curr_user.username
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).decode_netloc() != '':
            next_page = '/'

        session['username'] = user.username
        session['userid'] = user.id

        return redirect(next_page)
    
    return render_template('module_auth/login.html', title='Log in', form=form)


@module_auth.route('/logout/', methods=['GET'])
def logout():
    logout_user()
    return redirect('/')


@module_auth.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registerd user!')
        return redirect(url_for('auth.login'))

    return render_template('module_auth/register.html', title='Register', form=form)
