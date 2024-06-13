from flask import Blueprint, request, jsonify
from utils.auth import token_required
from services.messaging_service import MessagingService

messaging_api = Blueprint('messaging_api', __name__)

@messaging_api.route('/messages', methods=['POST'])
@token_required
def send_message():
    data = request.get_json()
    if not data or 'sender_id' not in data or 'recipient_id' not in data or 'content' not in data:
        return jsonify({'error': 'Sender ID, recipient ID, and content are required'}), 400
    message = MessagingService.send_message(data)
    return jsonify(message), 201

@messaging_api.route('/messages/<int:message_id>', methods=['GET'])
@token_required
def get_message(message_id):
    message = MessagingService.get_message(message_id)
    if message:
        return jsonify(message), 200
    return jsonify({'error': 'Message not found'}), 404

@messaging_api.route('/messages/user/<int:user_id>', methods=['GET'])
@token_required
def get_messages_by_user(user_id):
    messages = MessagingService.get_messages_by_user(user_id)
    return jsonify(messages), 200