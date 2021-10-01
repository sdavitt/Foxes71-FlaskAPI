from functools import wraps
from flask import request, jsonify

from app.models import User

# here we are creating the @token_required decorator for protecting our API routes

def token_required(a_function):
    @wraps(a_function)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            print(token)
        if not token:
            return jsonify({'message': 'Missing authorization token. Please register as a user to use CUD endpoints.'}), 401
        
        x = User.query.filter_by(apitoken=token).first()
        if not x:
            return jsonify({'message': 'Incorrect authorization token. Please register as a user to use CUD endpoints.'}), 401

        return a_function(*args, **kwargs)
    return decorated
