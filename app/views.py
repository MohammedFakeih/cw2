from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView
from flask_security import login_required

from app import app, db, admin, user_datastore
from .models import Review, User, Book

@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='jon@gmail.net', username='jsnow', password='password')
    db.session.commit()

@app.route('/')
@login_required
def home():
    return render_template('index.html')
