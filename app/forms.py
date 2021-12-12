from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, PasswordField, SelectField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms.fields.html5 import DateField

class UserRegister(FlaskForm):
    username = StringField('Usernane', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(),
        Length(min=5, max=16, 'Password must be between 5 and 16 characters'),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat password')

class UserLogin(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class ReviewForm(FlaskForm):
    userRating = SelectField('User rating', choices=[i for i in range(1, 11)],
        coerce=int, validators=[InputRequired()])
    isFinished = BooleanField('Finished reading')
    startDate = DateField('Start date')
    finishDate = DateField('Finish date')
    review = TextAreaField('Review', validators=[Length(max=1000)])
