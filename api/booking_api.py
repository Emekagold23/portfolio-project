from flask import Blueprint, request, jsonify
from utils.auth import token_required
from services.booking_service import BookingService

booking_api = Blueprint('booking_api', __name__)

@booking_api.route('/api/bookings', methods=['POST'])
@token_required
def create_booking(user_id):
    data = request.json
    if not data.get('job_id') or not data.get('scheduled_time'):
        return jsonify({'error': 'Please provide job_id and scheduled_time'}), 400
    
    booking = BookingService.create_booking(user_id, data['job_id'], data['scheduled_time'])
    if booking:
        return jsonify(booking.to_dict()), 201
    else:
        return jsonify({'error': 'Booking could not be created'}), 500

@booking_api.route('/api/bookings/<int:booking_id>', methods=['GET'])
@token_required
def get_booking(user_id, booking_id):
    booking = BookingService.get_booking(booking_id)
    if booking:
        return jsonify(booking.to_dict()), 200
    return jsonify({'error': 'Booking not found'}), 404

@booking_api.route('/api/bookings/user/<int:user_id>', methods=['GET'])
@token_required
def get_bookings_by_user(user_id):
    bookings = BookingService.get_bookings_by_user(user_id)
    if bookings:
        return jsonify([booking.to_dict() for booking in bookings]), 200
    return jsonify({'error': 'No bookings found for this user'}), 404

@booking_api.route('/api/bookings/<int:booking_id>', methods=['PUT'])
@token_required
def update_booking(user_id, booking_id):
    data = request.json
    booking = BookingService.update_booking(booking_id, data)
    if booking:
        return jsonify(booking.to_dict()), 200
    return jsonify({'error': 'Booking not found or could not be updated'}), 404

@booking_api.route('/api/bookings/<int:booking_id>', methods=['DELETE'])
@token_required
def delete_booking(user_id, booking_id):
    result = BookingService.delete_booking(booking_id)
    if result:
        return jsonify({'message': 'Booking deleted successfully'}), 200
    return jsonify({'error': 'Booking not found'}), 404
