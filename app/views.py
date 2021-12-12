from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView
from flask_security import login_required, current_user
from flask_security.utils import hash_password

from .forms import ReviewForm
from app import app, db, admin, user_datastore, security
from .models import Review, User, Book
import math

@app.route('/')
def home():
    welcome = "Sign in"
    isAuth = False
    userId = -1
    if current_user.is_authenticated:
        welcome = "Welcome, " + current_user.username
        isAuth = True
        userId = current_user.id
    books = {}
    for b in Book.query.all():
        adjustedRating = round(b.avgRating)
        full = int(adjustedRating)
        empty = 10 - full
        books.update({b: (full, empty)})
    return render_template('index.html', title='MyBooks', welcome=welcome,
                            books=books, isAuth=isAuth, id=userId)

@app.route('/user', methods=['GET', 'POST'])
@login_required
def user_profile():
    return render_template('index.html')

@security.login_context_processor
def security_login_processor():
    return dict(title="Login")

@app.route('/book/<id>/reviews', methods=['GET', 'POST'])
def book_reviews(id):
    book = Book.query.filter_by(id=id).first()
    adjustedRating = round(book.avgRating)
    full = int(adjustedRating)
    empty = 10 - full
    reviews = {}
    for r in book.users:
        username = User.query.filter_by(id=r.userId).first().username
        reviews.update({r: username})
    return render_template('book_reviews.html', title=book.title, reviews=reviews, book=book, full=full, empty=empty)

@app.route('/user/<id>/reviews', methods=['GET', 'POST'])
@login_required
def user_reviews(id):
    reviews = {}
    for r in current_user.users:
        title = Book.query.filter_by(id=r.bookId).first().title
        reviews.update({r: title})
    return render_template('your_reviews.html', title='Your reviews', user=current_user, reviews=reviews)

@app.route('/book/<id>/create_review', methods=['GET', 'POST'])
@login_required
def create_review(id):
    form = ReviewForm()
    if form.validate_on_submit():
        b = Book.query.filter_by(id=id).first()
        r = Review(userId=current_user.id, bookId=id)
        r.userRating = form.userRating.data
        r.startDate = form.startDate.data
        r.finishDate = form.finishDate.data
        r.isFinished = form.isFinished.data
        r.review = form.review.data
        b.users.append(r)
        current_user.books.append(r)
        db.session.commit()
        console.log('Review added')
    return render_template('review_form.html', title='Create a review',  review_form=form)
