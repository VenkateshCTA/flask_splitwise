#################
#### imports ####
#################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlite3

################
#### config ####
################

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.secret_key = 'Venki_cta1'
app.config['SESSION_TYPE'] = 'filesystem'
APP_SETTINGS="config.DevelopmentConfig"
db = SQLAlchemy(app)
#db = sqlite3.connect('sample.db')

from project.users.views import users_blueprint
from project.home.views import home_blueprint

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


from models import User

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
