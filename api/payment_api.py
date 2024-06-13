from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound
from utils.auth import token_required
from services.payment_service import PaymentService

payment_api = Blueprint('payment_api', __name__)

@payment_api.route('/payments', methods=['POST'])
@token_required
def create_payment(user_id):
    data = request.get_json()
    if not data:
        raise BadRequest(description='Invalid input data')
    data['user_id'] = user_id  # Ensure the user ID is included in the payment data
    payment = PaymentService.create_payment(data)
    return jsonify(payment), 201

@payment_api.route('/payments/<int:payment_id>', methods=['GET'])
@token_required
def get_payment(user_id, payment_id):
    payment = PaymentService.get_payment(payment_id)
    if not payment:
        raise NotFound(description='Payment not found')
    return jsonify(payment)

@payment_api.route('/payments/user/<int:user_id>', methods=['GET'])
@token_required
def get_payments_by_user(user_id):
    payments = PaymentService.get_payments_by_user(user_id)
    if not payments:
        raise NotFound(description='No payments found for the user')
    return jsonify(payments)
