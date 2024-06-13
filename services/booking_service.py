from models import db, Booking

class BookingService:
    @staticmethod
    def create_booking(user_id, job_id, scheduled_time):
        new_booking = Booking(
            user_id=user_id,
            job_id=job_id,
            scheduled_time=scheduled_time
        )
        db.session.add(new_booking)
        db.session.commit()
        return new_booking

    @staticmethod
    def get_booking(booking_id):
        return Booking.query.get(booking_id)

    @staticmethod
    def get_bookings_by_user(user_id):
        return Booking.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update_booking(booking_id, data):
        booking = Booking.query.get(booking_id)
        if booking:
            booking.job_id = data.get('job_id', booking.job_id)
            booking.scheduled_time = data.get('scheduled_time', booking.scheduled_time)
            db.session.commit()
        return booking

    @staticmethod
    def delete_booking(booking_id):
        booking = Booking.query.get(booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return True
        return False
