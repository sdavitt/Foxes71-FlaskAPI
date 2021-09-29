# imports that I'll need to work with WTForms: generic form template, whatever types of data fields you intend to use, and whatever validators you intend to use
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, PasswordField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo

# creating a new form - we're going to be making a class that inherits some behavior from FlaskForm

class newActorForm(FlaskForm):
    # what we put inside this class is whatever data fields we intend our form to have
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name')
    hiringprice = StringField('Hiring Price')
    age = IntegerField('Age', validators=[DataRequired()])
    nationality = StringField('Nationality')
    bestrole = StringField('Best Role', validators=[DataRequired()])
    bestmovie = StringField('Best Movie/Show', validators=[DataRequired()])
    submit = SubmitField()

class signInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()

class signUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField()

class updateUser(FlaskForm):
    newusername = StringField('New Username')
    newpassword = PasswordField('New Password')
    confirm_newpassword = PasswordField('Confirm New Password', validators=[EqualTo('newpassword')])
    oldpassword = PasswordField('Current Password', validators=[DataRequired()])
    submit = SubmitField()