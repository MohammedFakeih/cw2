from app import db

class Review (db.Model):
    userId = db.Column(db.ForeignKey('user.id'), primary_key=True)
    bookId = db.Column(db.ForeignKey('book.id'), primary_key=True)
    userRating = db.Column(db.Integer)
    isReading = db.Column(db.Boolean)
    startReading = db.Column(db.DateTime)
    finishReading = db.Column(db.DateTime)
    review = db.Column(db.String(500))
    user = db.relationship('User', back_populates='books')
    book = db.relationship('Book', back_populates='users')

    def __repr__(self):
        return self.userId + ' ' + self.bookId

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), index=True, unique=True)
    password = db.Column(db.String(250))
    booksRead = db.Column(db.Integer)
    books = db.relationship('Review', back_populates='user')

    def __repr__(self):
        return self.username

class Book (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), index=True)
    author = db.Column(db.String(250), index=True)
    image = db.Column(db.String(250))
    avgRating = db.Column(db.Float)
    users = db.relationship('Review', back_populates='book')

    def __repr__(self):
        return self.title
