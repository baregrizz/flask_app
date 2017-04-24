import os.path

SECRET_KEY = 'DuzheSecretno!'
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')