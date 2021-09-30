# if using a run.py file for your shell context processor, you must change FLASK_APP in .env to =run.py

from app import app
from app.models import db, User, Actor
from app.api.routes import actors

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, 'Actor': Actor, 'ActorRoute': actors}