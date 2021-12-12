from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_admin import Admin
from flask_security import Security, SQLAlchemyUserDatastore
import logging
import click


app = Flask(__name__)
app.config.from_object('config')

csrf = CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

logging.basicConfig(filename='myapp.log', level=logging.DEBUG,
                    format='[%(asctime)s]%(levelname)s:%(message)s')

admin = Admin(app,template_mode='bootstrap3')

from app import models
from .forms import ExtendedRegisterForm

user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore, register_form=ExtendedRegisterForm)

admin.add_view(models.UserModelView(models.User, db.session))
admin.add_view(models.UserModelView(models.Book, db.session))
admin.add_view(models.UserModelView(models.Review, db.session))

from app import views

@app.cli.command('create-admin')
def create_admin():
    a = user_datastore.create_user(email='admin', username='admin', password='loophole')
    r = user_datastore.create_role(name='Admin', description='Has access to admin pages')
    user_datastore.add_role_to_user(a, r)
    db.session.commit()
    return 'Done'
