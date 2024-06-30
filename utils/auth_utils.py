from functools import wraps
from flask import request, jsonify, current_app, Blueprint
import jwt

auth_bp = Blueprint('auth_bp', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 403
        
        return f(*args, **kwargs)
    return decorated

# Example usage of the auth blueprint
@auth_bp.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'This is a protected route'})
