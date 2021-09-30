from flask import Blueprint, json, jsonify
from app.models import Actor, db

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/actors', methods=['GET'])
def actors():
    """
    [GET] /api/actors
    Returns JSON data about all actors in our database
    """
    actors = {(a.first_name+' '+a.last_name).strip():a.to_dict() for a in Actor.query.all()}
    return jsonify(actors)