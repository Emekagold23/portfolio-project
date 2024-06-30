import pytest
from app import create_app, db
from models import User, Job, Booking, Review, Message, Notification, Payment, Geolocation

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            # Create all tables
            db.create_all()
            yield testing_client  # this is where the testing happens!

            # Drop all tables
            db.drop_all()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table(s)
    db.create_all()

    # Insert user data
    user1 = User(username='test_user1', email='test1@example.com', user_type='client', password='password')
    user2 = User(username='test_worker1', email='worker1@example.com', user_type='worker', password='password')
    db.session.add(user1)
    db.session.add(user2)

    # Insert job data
    job1 = Job(title='Test Job 1', description='Test job description 1', client_id=user1.id, worker_id=user2.id)
    db.session.add(job1)

    # Insert payment data
    payment1 = Payment(client_id=user1.id, worker_id=user2.id, amount=100.0, status='completed')
    db.session.add(payment1)

    # Insert geolocation data
    geolocation1 = Geolocation(user_id=user2.id, latitude=40.7128, longitude=-74.0060)
    db.session.add(geolocation1)

    # Commit the changes for the users, job, payment, and geolocation
    db.session.commit()

    yield db  # this is where the testing happens!

    db.session.remove()
    db.drop_all()

def test_user_model(init_database):
    user = User.query.filter_by(email='test1@example.com').first()
    assert user.username == 'test_user1'
    assert user.check_password('password') == True

def test_job_model(init_database):
    job = Job.query.filter_by(title='Test Job 1').first()
    assert job.description == 'Test job description 1'
    assert job.client.username == 'test_user1'
    assert job.worker.username == 'test_worker1'

def test_booking_model(init_database):
    user = User.query.filter_by(email='test1@example.com').first()
    job = Job.query.filter_by(title='Test Job 1').first()
    booking = Booking(client_id=user.id, job_id=job.id)
    db.session.add(booking)
    db.session.commit()

    assert booking in db.session
    assert booking.client_id == user.id
    assert booking.job_id == job.id

def test_review_model(init_database):
    user = User.query.filter_by(email='test1@example.com').first()
    worker = User.query.filter_by(email='worker1@example.com').first()
    review = Review(reviewer_id=user.id, reviewee_id=worker.id, rating=5, comment='Great job!')
    db.session.add(review)
    db.session.commit()

    assert review in db.session
    assert review.rating == 5
    assert review.comment == 'Great job!'
    assert review.reviewer_id == user.id
    assert review.reviewee_id == worker.id

def test_message_model(init_database):
    user = User.query.filter_by(email='test1@example.com').first()
    worker = User.query.filter_by(email='worker1@example.com').first()
    message = Message(sender_id=user.id, receiver_id=worker.id, content='Hello, can you help me?')
    db.session.add(message)
    db.session.commit()

    assert message in db.session
    assert message.content == 'Hello, can you help me?'
    assert message.sender_id == user.id
    assert message.receiver_id == worker.id

def test_notification_model(init_database):
    user = User.query.filter_by(email='test1@example.com').first()
    notification = Notification(user_id=user.id, message='This is a test notification.')
    db.session.add(notification)
    db.session.commit()

    assert notification in db.session
    assert notification.message == 'This is a test notification.'
    assert notification.user_id == user.id

def test_payment_model(init_database):
    payment = Payment.query.filter_by(amount=100.0).first()
    assert payment.status == 'completed'
    assert payment.amount == 100.0

def test_geolocation_model(init_database):
    geolocation = Geolocation.query.filter_by(latitude=40.7128).first()
    assert geolocation.longitude == -74.0060
    assert geolocation.latitude == 40.7128
