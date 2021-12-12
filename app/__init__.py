from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin
from flask_security import Security, SQLAlchemyUserDatastore
import logging


app = Flask(__name__)
app.config.from_object('config')

Bootstrap(app)
csrf = CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

logging.basicConfig(filename='myapp.log', level=logging.DEBUG,
                    format='[%(asctime)s]%(levelname)s:%(message)s')

admin = Admin(app,template_mode='bootstrap3')

from app import models

user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)

from app import views
