from flask import abort
from flask_login import current_user


def check_admin():
    if not current_user.is_admin:
        abort(403)
