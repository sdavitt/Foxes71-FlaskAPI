# imports that I'll need to work with WTForms: generic form template, whatever types of data fields you intend to use, and whatever validators you intend to use
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired

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