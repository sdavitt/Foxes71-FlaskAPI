# if using a run.py file for your shell context processor, you must change FLASK_APP in .env to =run.py

from app import app
from app.models import db, User, Actor

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, 'Actor': Actor}