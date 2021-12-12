from app import db
from flask_security import UserMixin, RoleMixin, current_user
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for

class UserModelView(ModelView):
  def is_accessible(self):
    return (current_user.is_active and
            current_user.is_authenticated and
            current_user.has_role('Admin'))

  def _handle_view(self, name):
    if not self.is_accessible():
      return redirect(url_for('security.login'))


class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer, db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Review (db.Model):
    userId = db.Column(db.ForeignKey('user.id'), primary_key=True)
    bookId = db.Column(db.ForeignKey('book.id'), primary_key=True)
    userRating = db.Column(db.Integer)
    isFinished = db.Column(db.Boolean)
    startReading = db.Column(db.DateTime)
    finishReading = db.Column(db.DateTime)
    review = db.Column(db.String(500))
    user = db.relationship('User', back_populates='books')
    book = db.relationship('Book', back_populates='users')

    def __repr__(self):
        return self.userId + ' ' + self.bookId

class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    username = db.Column(db.String(250), index=True)
    password = db.Column(db.String(250))
    active = db.Column(db.Boolean)
    books = db.relationship('Review', back_populates='user')
    roles = db.relationship('Role', secondary='roles_users',
                         backref='users', lazy='dynamic')

    def __repr__(self):
        return self.username

class Book (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), index=True)
    author = db.Column(db.String(250), index=True)
    image = db.Column(db.String(250))
    description = db.Column(db.String(500))
    avgRating = db.Column(db.Float)
    users = db.relationship('Review', back_populates='book')

    def __repr__(self):
        return self.title
