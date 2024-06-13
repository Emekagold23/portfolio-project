from flask import Blueprint, render_template, request, redirect, url_for
from models import Booking, db

booking_routes = Blueprint('booking_routes', __name__)

@booking_routes.route('/bookings', methods=['GET'])
def bookings_page():
    bookings = Booking.query.all()
    return render_template('bookings.html', bookings=bookings)

@booking_routes.route('/bookings/<int:booking_id>', methods=['GET'])
def booking_page(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    return render_template('booking.html', booking=booking)

@booking_routes.route('/bookings/create', methods=['GET', 'POST'])
def create_booking_page():
    if request.method == 'POST':
        data = request.form
        new_booking = Booking(
            user_id=data['user_id'],
            job_id=data['job_id'],
            scheduled_time=data['scheduled_time']
        )
        db.session.add(new_booking)
        db.session.commit()
        return redirect(url_for('booking_routes.bookings_page'))
    return render_template('create_booking.html')
