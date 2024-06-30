from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound
from utils.auth_utils import token_required
from services.payment_service import PaymentService

payment_api = Blueprint('payment_api', __name__)

# Create a new payment
@payment_api.route('/payments', methods=['POST'])
@token_required
def create_payment():
    data = request.get_json()
    if not data:
        raise BadRequest(description='Invalid input data')
    payment = PaymentService.create_payment(data)
    return jsonify(payment), 201

# Get a payment by ID
@payment_api.route('/payments/<int:payment_id>', methods=['GET'])
@token_required
def get_payment(payment_id):
    payment = PaymentService.get_payment(payment_id)
    if not payment:
        raise NotFound(description='Payment not found')
    return jsonify(payment)

# Update a payment by ID
@payment_api.route('/payments/<int:payment_id>', methods=['PUT'])
@token_required
def update_payment(payment_id):
    data = request.get_json()
    if not data:
        raise BadRequest(description='Invalid input data')
    payment = PaymentService.update_payment(payment_id, data)
    if not payment:
        raise NotFound(description='Payment not found')
    return jsonify(payment)

# Delete a payment by ID
@payment_api.route('/payments/<int:payment_id>', methods=['DELETE'])
@token_required
def delete_payment(payment_id):
    success = PaymentService.delete_payment(payment_id)
    if not success:
        raise NotFound(description='Payment not found')
    return jsonify({'message': 'Payment deleted successfully'})

# Get all payments
@payment_api.route('/payments', methods=['GET'])
@token_required
def get_payments():
    payments = PaymentService.get_all_payments()
    return jsonify(payments)
