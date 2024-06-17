from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.services.profile_service import ProfileService
from utils.auth_utils import token_required

profile_api = Blueprint('profile_api', __name__)

@profile_api.route('/profile', methods=['GET', 'POST'])
@token_required
@login_required
def profile():
    if request.method == 'POST':
        data = request.get_json()
        updated_profile = ProfileService.update_profile(current_user, data)
        return jsonify(updated_profile), 200
    
    profile_data = current_user.profile.to_dict() if current_user.profile else {}
    return jsonify(profile_data), 200