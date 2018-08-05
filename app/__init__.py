from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from datetime import timedelta
from flask_admin.contrib.sqla import ModelView
from flask_debugtoolbar import DebugToolbarExtension
from flask_socketio import SocketIO, emit

socketio = SocketIO()

app = Flask(__name__)

app.config.from_object(Config)
app.config['DEBUG'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)
socketio.init_app(app)

toolbar = DebugToolbarExtension(app)
login = LoginManager(app)
login.login_view = 'auth.login'

admin = Admin(app, template_mode='bootstrap3')

    
@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


from app.module_auth.controllers import module_auth as auth_module
from app.module_main.controllers import module_main as main_module
from app.module_task.controllers import module_task as task_module
from app.module_role.controllers import module_role as role_module
from app.module_role.controllers import module_userrole as user_role_module


app.register_blueprint(auth_module)
app.register_blueprint(main_module)
app.register_blueprint(task_module)
app.register_blueprint(role_module)
app.register_blueprint(user_role_module)

# from app.module_auth.models import User, Role, UserRole
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Role, db.session))
# admin.add_view(ModelView(UserRole, db.session))

db.create_all()
