import pytest
from flask import Flask
from app.forms import LoginForm, RegistrationForm, BookingForm, ReviewForm, AdminForm, MessagingForm
from wtforms import ValidationError

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SECRET_KEY'] = 'secret'
    return app

# Utility function for creating a form
def create_form(form_class, **kwargs):
    return form_class(**kwargs)

# Tests for LoginForm
def test_login_form_valid_data(app):
    form = create_form(LoginForm, email="test@example.com", password="password")
    assert form.validate() is True

def test_login_form_missing_email(app):
    form = create_form(LoginForm, password="password")
    assert form.validate() is False
    assert 'email' in form.errors

def test_login_form_missing_password(app):
    form = create_form(LoginForm, email="test@example.com")
    assert form.validate() is False
    assert 'password' in form.errors

# Tests for RegistrationForm
def test_registration_form_valid_data(app):
    form = create_form(RegistrationForm, email="test@example.com", password="password", confirm="password")
    assert form.validate() is True

def test_registration_form_missing_email(app):
    form = create_form(RegistrationForm, password="password", confirm="password")
    assert form.validate() is False
    assert 'email' in form.errors

def test_registration_form_password_mismatch(app):
    form = create_form(RegistrationForm, email="test@example.com", password="password", confirm="different")
    assert form.validate() is False
    assert 'confirm' in form.errors

# Tests for BookingForm
def test_booking_form_valid_data(app):
    form = create_form(BookingForm, job_id=1, user_id=2, date="2023-05-19", time="14:00")
    assert form.validate() is True

def test_booking_form_missing_job_id(app):
    form = create_form(BookingForm, user_id=2, date="2023-05-19", time="14:00")
    assert form.validate() is False
    assert 'job_id' in form.errors

# Tests for ReviewForm
def test_review_form_valid_data(app):
    form =create_form(ReviewForm, reviewer_id=1, reviewee_id=2, rating=5, comment="Great job!")
    assert form.validate() is True

def test_review_form_missing_reviewer_id(app):
    form = create_form(ReviewForm, reviewee_id=2, rating=5, comment="Great job!")
    assert form.validate() is False
    assert 'reviewer_id' in form.errors

def test_review_form_invalid_rating(app):
    form = create_form(ReviewForm, reviewer_id=1, reviewee_id=2, rating=6, comment="Great job!")
    assert form.validate() is False
    assert 'rating' in form.errors

# Tests for AdminForm
def test_admin_form_valid_data(app):
    form = create_form(AdminForm, email="admin@example.com", password="adminpass")
    assert form.validate() is True

def test_admin_form_missing_email(app):
    form = create_form(AdminForm, password="adminpass")
    assert form.validate() is False
    assert 'email' in form.errors

# Tests for MessagingForm
def test_messaging_form_valid_data(app):
    form = create_form(MessagingForm, sender_id=1, recipient_id=2, content="Hello!")
    assert form.validate() is True

def test_messaging_form_missing_content(app):
    form = create_form(MessagingForm, sender_id=1, recipient_id=2)
    assert form.validate() is False
    assert 'content' in form.errors