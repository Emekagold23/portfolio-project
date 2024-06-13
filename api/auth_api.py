from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    user = AuthService.authenticate_user(data['email'], data['password'])
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'Invalid credentials'}), 401

@auth_api.route('/api/register', methods=['POST'])
def api_register():
    data = request.json
    user = AuthService.register_user(data['username'], data['email'], data['password'])
    if user:
        return jsonify(user.to_dict()), 201
    return jsonify({'error': 'Email already registered'}), 400