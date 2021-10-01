from flask import Blueprint, json, jsonify, request
from app.models import Actor, db
from .apiauthhelper import token_required


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/actors', methods=['GET'])
def actors():
    """
    [GET] /api/actors
    Returns JSON data about all actors in our database
    """
    actors = {(a.first_name+' '+a.last_name).strip():a.to_dict() for a in Actor.query.all()}
    return jsonify(actors)

@api.route('/actors/<int:id>', methods=['GET'])
def get_actor(id):
    """
    [GET] /api/actors/<int:id>
    Returns JSON data about a single actor with the specified ID
    """
    try:
        actor = Actor.query.get(id).to_dict()
        return jsonify(actor)
    except:
        return jsonify(f"Actor of id: <{id}> does not exist in the database.")

@api.route('/actors/<int:id>', methods=['DELETE'])
@token_required
def delete_actor(id):
    """
    [DELETE] /api/actors/<int:id>
    Removes an actor from our database based on the provided ID
    """
    try:
        actor = Actor.query.get(id)
        db.session.delete(actor)
        db.session.commit()
        return jsonify({'Deleted': actor.to_dict()})
    except:
        return jsonify(f"Actor of id: <{id}> does not exist in the database.")


@api.route('/actors/<int:id>', methods=['PUT'])
@token_required
def update_actor(id):
    """
    [PUT] /actors/<int:id>
    Accepts input of a dictionary of as many or as few attributes of the specified actor to update
    Attribute options: 'id', 'first_name', 'last_name', 'age', 'nationality', 'bestrole', 'bestmovie', 'hiringprice'
    Returns a dictionary representation of the updated actor
    """
    r = request.get_json()
    print(r)
    actor = Actor.query.get(id)
    # basically we'll update our actor object using a helper function :)
    actor.from_dict(r)
    print(actor.to_dict())
    db.session.commit()
    return jsonify({'Updated': actor.to_dict()})

@api.route('createactor', methods=['POST'])
@token_required
def create_actor():
    """
    [POST] /api/createactor
    Accepts input of JSON data for an actor in the format:
    {
        'first_name': <string>,
        'last_name': <string>,
        'age': <integer>,
        'nationality': <string>,
        'bestrole': <string>,
        'bestmovie': <string>,
        'hiringprice': <string>
    }
    Creates said actor in our database with a serial integer id
    Returns dictionary representation of the actor in the database
    """
    r = request.get_json()
    newactor = Actor()
    newactor.from_dict(r)
    print(newactor.to_dict())
    db.session.add(newactor)
    db.session.commit()
    return jsonify({'Created': Actor.query.all()[-1].to_dict()})

