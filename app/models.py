from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from datetime import datetime
import uuid

# adding flask security for password
from werkzeug.security import generate_password_hash

# instantiate an instance of our login manager
login = LoginManager()

# necessary user_loader function that our Login manager relies upon for some current_user operations
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)



# instantiate an instance of our ORM to handle database communication
db = SQLAlchemy()

# define a model - a model is going to be an entity/a table in our database
# and we define it with the SQL CREATE TABLE in mind (what columns do I want? what SQL datatypes will those columns be? what constraints will those columns have?)
class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    hiringprice = db.Column(db.String(20))
    age = db.Column(db.Integer)
    nationality = db.Column(db.String(50))
    bestrole = db.Column(db.String(100))
    bestmovie = db.Column(db.String(100))

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'hiringprice': self.hiringprice,
            'age': self.age,
            'nationality': self.nationality,
            'bestrole': self.bestrole,
            'bestmovie': self.bestmovie
        }

    def from_dict(self, new):
        if new.get('id'):
            self.id = new.get('id')
        if new.get('first_name'):
            self.first_name = new.get('first_name')
        if new.get('last_name') or new.get('last_name') == '':
            self.last_name = new.get('last_name')
        if new.get('hiringprice') or new.get('hiringprice') == '':
            self.hiringprice = new.get('hiringprice')
        if new.get('age'):
            self.age = new.get('age')
        if new.get('nationality') or new.get('nationality') == '':
            self.nationality = new.get('nationality')
        if new.get('bestrole'):
            self.bestrole = new.get('bestrole')
        if new.get('bestmovie'):
            self.bestmovie = new.get('bestmovie')


# for our user model we'll need a couple additional tools - specifically, a login manager and a security package
class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable=True, default='')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower()
        self.password = generate_password_hash(password)
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid.uuid4())

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'date_created': self.date_created
        }