import pytest
from flask import url_for
from app import create_app, db
from app.models import User, Job, Payment, Geolocation, Review, Message, Booking, Notification

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

    # Insert review data
    review1 = Review(reviewer_id=user1.id, reviewee_id=user2.id, rating=5, comment='Great job!')
    db.session.add(review1)

    # Insert message data
    message1 = Message(sender_id=user1.id, receiver_id=user2.id, content='Hello, can you help me?')
    db.session.add(message1)

    # Insert booking data
    booking1 = Booking(client_id=user1.id, job_id=job1.id)
    db.session.add(booking1)

    # Insert notification data
    notification1 = Notification(user_id=user1.id, message='This is a test notification.')
    db.session.add(notification1)

    # Commit the changes for the users, job, payment, geolocation, review, message, booking, and notification
    db.session.commit()

    yield db  # this is where the testing happens!

    db.session.remove()
    db.drop_all()

def test_home_page(test_client):
    response = test_client.get(url_for('main.index'))
    assert response.status_code == 200
    assert b"Welcome to WorkPal" in response.data

def test_register_page(test_client):
    response = test_client.get(url_for('auth.register'))
    assert response.status_code == 200
    assert b"Register" in response.data

def test_login_page(test_client):
    response = test_client.get(url_for('auth.login'))
    assert response.status_code == 200
    assert b"Login" in response.data

def test_user_profile_page(test_client, init_database):
    user = User.query.filter_by(email='test1@example.com').first()
    login_response = test_client.post(url_for('auth.login'), data=dict(email='test1@example.com', password='password'), follow_redirects=True)
    assert login_response.status_code == 200

    response = test_client.get(url_for('user.profile', user_id=user.id))
    assert response.status_code == 200
    assert b"test_user1" in response.data

def test_job_details_page(test_client, init_database):
    job = Job.query.filter_by(title='Test Job 1').first()
    response = test_client.get(url_for('job.job_details', job_id=job.id))
    assert response.status_code == 200
    assert b"Test Job 1" in response.data

def test_payment_processing(test_client, init_database):
    response = test_client.post(url_for('payment.process_payment'), data=dict(client_id=1, worker_id=2, amount=50.0), follow_redirects=True)
    assert response.status_code == 200
    assert b"Payment processed" in response.data

def test_geolocation_update(test_client, init_database):
    response = test_client.post(url_for('geolocation.update_location'), data=dict(user_id=2, latitude=37.7749, longitude=-122.4194), follow_redirects=True)
    assert response.status_code == 200
    assert b"Location updated" in response.data

def test_review_submission(test_client, init_database):
    response = test_client.post(url_for('review.submit_review'), data=dict(reviewer_id=1, reviewee_id=2, rating=5, comment='Excellent work!'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Review submitted" in response.data

def test_messaging(test_client, init_database):
    response = test_client.post(url_for('messaging.send_message'), data=dict(sender_id=1, receiver_id=2, content='Can you assist me with this task?'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Message sent" in response.data

def test_booking_creation(test_client, init_database):
    response = test_client.post(url_for('booking.create_booking'), data=dict(client_id=1, job_id=1), follow_redirects=True)
    assert response.status_code == 200
    assert b"Booking created" in response.data

def test_notification(test_client, init_database):
    response = test_client.post(url_for('notification.create_notification'), data=dict(user_id=1, message='You have a new task assigned.'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Notification created" in response.data

def test_admin_dashboard(test_client, init_database):
    response = test_client.get(url_for('admin.admin_dashboard'))
    assert response.status_code == 200
    assert b"Admin Dashboard" in response.data

import pytest
from flask import url_for
from app import create_app, db
from app.models import User, Job

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    user1 = User(email='test1@example.com', password='password')
    user2 = User(email='worker1@example.com', password='password')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    job1 = Job(title='Test Job 1', description='Job description', client_id=user1.id)
    db.session.add(job1)
    db.session.commit()

    yield db

    db.drop_all()

def test_home_page(test_client):
    response = test_client.get(url_for('main.index'))
    assert response.status_code == 200
    assert b"Welcome to WorkPal" in response.data

def test_register_page(test_client):
    response = test_client.get(url_for('auth.register'))
    assert response.status_code == 200
    assert b"Register" in response.data

def test_login_page(test_client):
    response = test_client.get(url_for('auth.login'))
    assert response.status_code == 200
    assert b"Log In" in response.data

def test_user_profile_page(test_client, init_database):
    test_client.post(url_for('auth.login'), data=dict(email='test1@example.com', password='password'), follow_redirects=True)
    response = test_client.get(url_for('user.profile', user_id=1))
    assert response.status_code == 200
    assert b"Profile" in response.data

def test_job_details_page(test_client, init_database):
    response = test_client.get(url_for('job.job_details', job_id=1))
    assert response.status_code == 200
    assert b"Test Job 1" in response.data

def test_payment_processing(test_client, init_database):
    response = test_client.post(url_for('payment.process_payment'), data=dict(job_id=1, amount=100), follow_redirects=True)
    assert response.status_code == 200
    assert b"Payment processed" in response.data

def test_geolocation_update(test_client, init_database):
    response = test_client.post(url_for('geolocation.update_location'), data=dict(user_id=1, latitude=40.7128, longitude=-74.0060), follow_redirects=True)
    assert response.status_code == 200
    assert b"Location updated" in response.data

def test_review_submission(test_client, init_database):
    response = test_client.post(url_for('review.submit_review'), data=dict(reviewer_id=1, reviewee_id=2, rating=4, comment='Good work!'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Review submitted" in response.data

def test_messaging(test_client, init_database):
    response = test_client.post(url_for('messaging.send_message'), data=dict(sender_id=1, recipient_id=2, content='Hello!'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Message sent" in response.data

def test_create_booking(test_client, init_database):
    response = test_client.post(url_for('booking.create_booking'), data=dict(job_id=1, user_id=2), follow_redirects=True)
    assert response.status_code == 200
    assert b"Booking created" in response.data

def test_create_notification(test_client, init_database):
    response = test_client.post(url_for('notification.create_notification'), data=dict(user_id=1, message='You have a new message'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Notification created" in response.data

def test_admin_dashboard(test_client, init_database):
    test_client.post(url_for('auth.login'), data=dict(email='admin@example.com', password='password'), follow_redirects=True)
    response = test_client.get(url_for('admin.dashboard'))
    assert response.status_code == 200
    assert b"Admin Dashboard" in response.data

def test_password_reset_request_page(test_client):
    response = test_client.get(url_for('auth.password_reset_request'))
    assert response.status_code == 200
    assert b"Password Reset" in response.data

def test_password_reset(test_client, init_database):
    response = test_client.post(url_for('auth.password_reset_request'), data=dict(email='test1@example.com'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Check your email for the instructions to reset your password" in response.data

def test_logout(test_client, init_database):
    test_client.post(url_for('auth.login'), data=dict(email='test1@example.com', password='password'), follow_redirects=True)
    response = test_client.get(url_for('auth.logout'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Log In" in response.data

def test_create_job(test_client, init_database):
    test_client.post(url_for('auth.login'), data=dict(email='test1@example.com', password='password'), follow_redirects=True)
    response = test_client.post(url_for('job.create_job'), data=dict(title='New Job', description='Job description', client_id=1), follow_redirects=True)
    assert response.status_code == 200
    assert b"Job created successfully" in response.data

def test_assign_job(test_client, init_database):
    test_client.post(url_for('auth.login'), data=dict(email='test1@example.com', password='password'), follow_redirects=True)
    response = test_client.post(url_for('job.assign_job'), data=dict(job_id=1, worker_id=2), follow_redirects=True)
    assert response.status_code == 200
    assert b"Job assigned successfully" in response.data

def test_complete_job(test_client, init_database):
    test_client.post(url_for('auth.login'), data=dict(email='worker1@example.com', password='password'), follow_redirects=True)
    response = test_client.post(url_for('job.complete_job'), data=dict(job_id=1), follow_redirects=True)
    assert response.status_code == 200
    assert b"Job marked as completed" in response.data

def test_search_jobs(test_client, init_database):
    response = test_client.get(url_for('search.jobs'), query_string={'q': 'Test Job'})
    assert response.status_code == 200
    assert b"Test Job 1" in response.data

def test_submit_report(test_client, init_database):
    response = test_client.post(url_for('report.submit_report'), data=dict(user_id=1, report_type='abuse', description='Inappropriate behavior'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Report submitted" in response.data

def test_404_error_handling(test_client):
    response = test_client.get('/non_existent_page')
    assert response.status_code == 404
    assert b"Page not found" in response.data

def test_star_rating_system(test_client, init_database):
    response = test_client.post(url_for('review.submit_review'), data=dict(reviewer_id=1, reviewee_id=2, rating=4, comment='Good work!'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Review submitted" in response.data

    response = test_client.get(url_for('review.get_reviews', user_id=2))
    assert response.status_code == 200
    assert b'4 stars' in response.data
