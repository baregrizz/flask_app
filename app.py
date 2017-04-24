from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_pyfile("config.py")

Bootstrap(app)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from views import *

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)