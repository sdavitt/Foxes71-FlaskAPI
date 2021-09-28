# os is a python built-in module that lets us do some operating system operations

import os

# we need to tell flask where the root directory for this project is
basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    """
    Set our configuration variables which tell the flask app how it is being set up to use what external functionality such as databases/mailing services/auth services
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABSE_URI') # reminder: add 'ql' to the end of 'postgres' to make 'postgresql' in the database_uri in the .env file
    SQLALCHEMY_TRACK_MODIFICATIONS = False