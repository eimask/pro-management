import os

DEBUG = False

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLE = True

CSRF_SESSION_KEY = "secret"


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'mysql+pymysql://root:ptMinh93@localhost/ProManagement'
    # 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
