import pytest
from models.booking import book_service, cancel_booking, get_user_bookings, get_worker_bookings
from unittest.mock import patch, MagicMock

# Sample data for testing
booking_data = {
    "user_id": 1,
    "worker_id": 2,
    "service_id": 123,
    "appointment_time": "2024-06-01 10:00:00",
    "duration": 2,  # in hours
    "notes": "Please bring necessary tools."
}

# Mock Booking Service
class MockBookingService:
    def book(self, user_id, worker_id, service_id, appointment_time, duration, notes):
        return {"status": "success", "booking_id": 12345}

    def cancel(self, booking_id):
        return {"status": "success", "message": "Booking canceled successfully"}

    def get_user_bookings(self, user_id):
        return {"status": "success", "bookings": [{"booking_id": 12345, "worker_id": 2, "service_id": 123, "appointment_time": "2024-06-01 10:00:00", "duration": 2, "notes": "Please bring necessary tools."}]}

    def get_worker_bookings(self, worker_id):
        return {"status": "success", "bookings": [{"booking_id": 12345, "user_id": 1, "service_id": 123, "appointment_time": "2024-06-01 10:00:00", "duration": 2, "notes": "Please bring necessary tools."}]}

# Patch the booking service in the booking module
@patch('app.booking.BookingService', new=MockBookingService)
def test_book_service():
    result = book_service(booking_data["user_id"], booking_data["worker_id"], booking_data["service_id"], booking_data["appointment_time"], booking_data["duration"], booking_data["notes"])
    assert result["status"] == "success"
    assert "booking_id" in result

@patch('app.booking.BookingService', new=MockBookingService)
def test_cancel_booking():
    booking_id = 12345  # Assume this is a valid booking ID
    result = cancel_booking(booking_id)
    assert result["status"] == "success"
    assert result["message"] == "Booking canceled successfully"

@patch('app.booking.BookingService', new=MockBookingService)
def test_get_user_bookings():
    user_id = 1
    result = get_user_bookings(user_id)
    assert result["status"] == "success"
    assert len(result["bookings"]) == 1

@patch('app.booking.BookingService', new=MockBookingService)
def test_get_worker_bookings():
    worker_id = 2
    result = get_worker_bookings(worker_id)
    assert result["status"] == "success"
    assert len(result["bookings"]) == 1