from flask import Blueprint, request, jsonify
from werkzeug.exceptions import NotFound, BadRequest
from models import User
from utils.auth import token_required
from services.user_service import UserService

user_api = Blueprint('user_api', __name__)

@user_api.route('/users', methods=['GET'])
@user_api.route('/users/<int:user_id>', methods=['GET'])
@token_required
def get_users(user_id=None):
    '''Gets the user with the given id or all users.'''
    if user_id:
        user = UserService.get_user_by_id(user_id)
        if user:
            return jsonify(user.to_dict())  # Assuming you have a to_dict method in the User model
        raise NotFound(description='User not found')
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users])

@user_api.route('/users/<int:user_id>', methods=['DELETE'])
@token_required
def remove_user(user_id):
    '''Removes a user with the given id.'''
    user = UserService.get_user_by_id(user_id)
    if user:
        UserService.delete_user(user)
        return jsonify({}), 200
    raise NotFound(description='User not found')

@user_api.route('/signup/client', methods=['POST'])
def signup_client():
    '''Adds a new client.'''
    try:
        data = request.get_json()
    except Exception:
        data = None
    if not data or not isinstance(data, dict):
        raise BadRequest(description='Not a JSON')
    if 'email' not in data:
        raise BadRequest(description='Missing email')
    if 'password' not in data:
        raise BadRequest(description='Missing password')
    if 'first_name' not in data:
        raise BadRequest(description='Missing first_name')
    if 'last_name' not in data:
        raise BadRequest(description='Missing last_name')

    user = UserService.create_user(data['first_name'], data['last_name'], data['email'], data['password'], 'client')
    return jsonify(user.to_dict()), 201

@user_api.route('/signup/worker', methods=['POST'])
def signup_worker():
    '''Adds a new worker.'''
    try:
        data = request.get_json()
    except Exception:
        data = None
    if not data or not isinstance(data, dict):
        raise BadRequest(description='Not a JSON')
    if 'email' not in data:
        raise BadRequest(description='Missing email')
    if 'password' not in data:
        raise BadRequest(description='Missing password')
    if 'first_name' not in data:
        raise BadRequest(description='Missing first_name')
    if 'last_name' not in data:
        raise BadRequest(description='Missing last_name')

    user = UserService.create_user(data['first_name'], data['last_name'], data['email'], data['password'], 'worker')
    return jsonify(user.to_dict()), 201

@user_api.route('/users/<int:user_id>', methods=['PUT'])
@token_required
def update_user(user_id):
    '''Updates the user with the given id.'''
    user = UserService.get_user_by_id(user_id)
    if user:
        try:
            data = request.get_json()
        except Exception:
            data = None
        if not data or not isinstance(data, dict):
            raise BadRequest(description='Not a JSON')
        updated_user = UserService.update_user(user, **data)
        return jsonify(updated_user.to_dict()), 200
    raise NotFound(description='User not found')
