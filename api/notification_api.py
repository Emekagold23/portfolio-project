from flask import Blueprint, request, jsonify
from utils.auth_utils import token_required
from services.notification_service import NotificationService

notification_api = Blueprint('notification_api', __name__)

@notification_api.route('/notifications', methods=['GET'])
@token_required
def get_notifications():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    notifications = NotificationService.get_notifications(user_id)
    return jsonify(notifications), 200

@notification_api.route('/notifications/<int:notification_id>', methods=['DELETE'])
@token_required
def delete_notification(notification_id):
    result = NotificationService.delete_notification(notification_id)
    if result:
        return jsonify({'message': 'Notification deleted successfully'}), 200
    else:
        return jsonify({'error': 'Notification not found'}), 404

@notification_api.route('/notifications', methods=['POST'])
@token_required
def create_notification():
    data = request.get_json()
    if not data or 'user_id' not in data or 'message' not in data:
        return jsonify({'error': 'User ID and message are required'}), 400
    notification = NotificationService.create_notification(data)
    return jsonify(notification), 201

