# imports - the Flask object which our app will be an instance of and the Config class we just made
from flask import Flask
from config import Config

# import our blueprints for registration
from .movies.routes import movies
from .authentication.routes import auth
from .api.routes import api

# imports for our database stuff
from .models import db, login
from flask_migrate import Migrate

# instantiate the instance of our application
app = Flask(__name__)

# register our blueprints
app.register_blueprint(movies)
app.register_blueprint(auth)
app.register_blueprint(api)

# configure that app from our config file
app.config.from_object(Config)

# configure our database to work with our app
db.init_app(app)

migrate = Migrate(app, db)

# configuration for our login manager
login.init_app(app)
login.login_view = 'auth.signin'
login.login_message = 'Please log in to see this page.'
login.login_message_category = 'alert-info'



# tell our newly instantiated app where it can find its traffic controller (aka routes) and where it can find its database models
from . import routes
from . import models
