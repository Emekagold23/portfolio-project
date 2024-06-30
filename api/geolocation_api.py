from flask import Blueprint, jsonify, request
from services.geolocation_service import GeolocationService
from utils.auth_utils import token_required

geolocation_api = Blueprint('geolocation_api', __name__)

@geolocation_api.route('/geolocation', methods=['POST'])
@token_required
def update_location():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400
    location, status_code = GeolocationService.update_location(data)
    if status_code == 404:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(location), 200