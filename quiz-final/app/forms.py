from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class CreateQuizForm(FlaskForm):
    quizname = TextAreaField('Enter Title', validators=[ DataRequired(), Length(min=1, max=64)])
    q1 = TextAreaField('Enter Question 1', validators=[ DataRequired(), Length(min=1, max=256)])
    q2 = TextAreaField('Enter Question 2', validators=[ DataRequired(), Length(min=1, max=256)])
    q3 = TextAreaField('Enter Question 3', validators=[ DataRequired(), Length(min=1, max=256)])
    submit = SubmitField('Submit')

class AnswerQuizForm(FlaskForm):
    #quizname = TextAreaField('Enter Title', validators=[ DataRequired(), Length(min=1, max=64)])
    a1 = TextAreaField('Input Q1', validators=[ DataRequired(), Length(min=1, max=256)])
    a2 = TextAreaField('Input Q1', validators=[ DataRequired(), Length(min=1, max=256)])
    a3 = TextAreaField('Input Q1', validators=[ DataRequired(), Length(min=1, max=256)])
    submit_name = TextAreaField('Input Q1', validators=[ DataRequired(), Length(min=1, max=64)])
    submit = SubmitField('Submit')