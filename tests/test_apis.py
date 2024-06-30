import pytest
from flask import url_for
from app import create_app, db
from models import User, Job

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

    user1 = User(email='client@example.com', password='password')
    user2 = User(email='worker@example.com', password='password')
    admin = User(email='admin@example.com', password='password', is_admin=True)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(admin)
    db.session.commit()

    job1 = Job(title='Test Job', description='Job description', client_id=user1.id)
    db.session.add(job1)
    db.session.commit()

    yield db

    db.drop_all()

# User API Tests
def test_get_users_api(test_client, init_database):
    response = test_client.get(url_for('user_api.get_users'))
    assert response.status_code == 200
    assert b'client@example.com' in response.data
    assert b'worker@example.com' in response.data

def test_create_user_api(test_client):
    response = test_client.post(url_for('user_api.create_user'), data=dict(email='new_user@example.com', password='password'), follow_redirects=True)
    assert response.status_code == 201
    assert b'User created successfully' in response.data

# Job API Tests
def test_get_jobs_api(test_client, init_database):
    response = test_client.get(url_for('job_api.get_jobs'))
    assert response.status_code == 200
    assert b'Test Job' in response.data

def test_create_job_api(test_client, init_database):
    response = test_client.post(url_for('job_api.create_job'), data=dict(title='New Job', description='New job description', client_id=1), follow_redirects=True)
    assert response.status_code == 201
    assert b'Job created successfully' in response.data

# Payment API Tests
def test_get_payments_api(test_client, init_database):
    response = test_client.get(url_for('payment_api.get_payments'))
    assert response.status_code == 200

def test_create_payment_api(test_client, init_database):
    response = test_client.post(url_for('payment_api.create_payment'), data=dict(job_id=1, amount=100), follow_redirects=True)
    assert response.status_code == 201
    assert b'Payment created successfully' in response.data

# Geolocation API Tests
def test_get_locations_api(test_client, init_database):
    response = test_client.get(url_for('geolocation_api.get_locations'))
    assert response.status_code == 200

def test_update_location_api(test_client, init_database):
    response = test_client.post(url_for('geolocation_api.update_location'), data=dict(user_id=1, latitude=40.7128, longitude=-74.0060), follow_redirects=True)
    assert response.status_code == 201
    assert b'Location updated successfully' in response.data

# Notification API Tests
def test_get_notifications_api(test_client, init_database):
    response = test_client.get(url_for('notification_api.get_notifications'))
    assert response.status_code == 200

def test_create_notification_api(test_client, init_database):
    response = test_client.post(url_for('notification_api.create_notification'), data=dict(user_id=1, message='You have a new message'), follow_redirects=True)
    assert response.status_code == 201
    assert b'Notification created successfully' in response.data

# Review API Tests
def test_get_reviews_api(test_client, init_database):
    response = test_client.get(url_for('review_api.get_reviews', user_id=2))
    assert response.status_code == 200

def test_submit_review_api(test_client, init_database):
    response = test_client.post(url_for('review_api.submit_review'), data=dict(reviewer_id=1, reviewee_id=2, rating=5, comment='Excellent work!'), follow_redirects=True)
    assert response.status_code == 201
    assert b'Review submitted successfully' in response.data

# Search API Tests
def test_search_jobs_api(test_client, init_database):
    response = test_client.get(url_for('search_api.search_jobs'), query_string={'q': 'Test Job'})
    assert response.status_code == 200
    assert b'Test Job' in response.data

# Report API Tests
def test_report_issue_api(test_client, init_database):
    response = test_client.post(url_for('report_api.report_issue'), data=dict(user_id=1, report_type='abuse', description='Inappropriate behavior'), follow_redirects=True)
    assert response.status_code == 201
    assert b'Report submitted successfully' in response.data

# Messaging API Tests
def test_get_messages_api(test_client, init_database):
    response = test_client.get(url_for('messaging_api.get_messages'))
    assert response.status_code == 200

def test_send_message_api(test_client, init_database):
    response = test_client.post(url_for('messaging_api.send_message'), data=dict(sender_id=1, recipient_id=2, content='Hello!'), follow_redirects=True)
    assert response.status_code == 201
    assert b'Message sent successfully' in response.data

# Booking API Tests
def test_create_booking_api(test_client, init_database):
    response = test_client.post(url_for('booking_api.create_booking'), data=dict(job_id=1, user_id=2), follow_redirects=True)
    assert response.status_code == 201
    assert b'Booking created successfully' in response.data

# Admin API Tests
def test_admin_get_users_api(test_client, init_database):
    test_client.post(url_for('auth.login'), data=dict(email='admin@example.com', password='password'), follow_redirects=True)
    response = test_client.get(url_for('admin_api.get_users'))
    assert response.status_code == 200
    assert b'client@example.com' in response.data
    assert b'worker@example.com' in response.data

def test_admin_get_jobs_api(test_client, init_database):
    test_client.post(url_for('auth.login'), data=dict(email='admin@example.com', password='password'), follow_redirects=True)
    response = test_client.get(url_for('admin_api.get_jobs'))
    assert response.status_code == 200
    assert b'Test Job' in response.data
