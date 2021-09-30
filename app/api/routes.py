from flask import Blueprint, jsonify
from app.models import Actor, db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/actors', methods=['GET'])
def actors():
    """
    [GET] /api/actors
    Provides a list of all actors in our database.
    """
    # query our database to get all of our current actor data and transform to a dictionary with a dictionary comprehension
    actors = {(a.first_name+' '+a.last_name).strip():a.to_dict() for a in Actor.query.all()}
    return jsonify(actors)