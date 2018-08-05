from flask import Blueprint, request, render_template, flash, g, sessions, redirect, url_for
from flask_login import login_required


module_main = Blueprint('main', __name__, url_prefix='')


@module_main.route('/', methods=['GET'])
@login_required
def index():
    return render_template('module_main/index.html', title='EasyManagement')
