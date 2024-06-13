from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def generate_token(user_id, expiration=3600):
    """Generate a JWT token for the given user ID."""
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'user_id': user_id}).decode('utf-8')


def verify_token(token):
    """Verify the JWT token and return the user ID if valid."""
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
        return data['user_id']
    except:
        return None


def login_required(func):
    """Decorator to require login for certain routes."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            user_id = verify_token(token)
            if not user_id:
                raise Exception
        except:
            return jsonify({'message': 'Token is invalid or expired'}), 401
        return func(user_id, *args, **kwargs)
    return decorated_function
