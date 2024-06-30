import pytest
from app import create_app, db
from config import TestingConfig
from models import User, Job, Booking
from datetime import datetime, timedelta

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()

@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    yield db
    db.drop_all()

@pytest.fixture(scope='function')
def new_user():
    user = User(first_name='Test', last_name='User', email='test.user@example.com', role='client')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture(scope='function')
def new_job():
    job = Job(title='Test Job', description='A test job', location='Test Location', budget=100)
    db.session.add(job)
    db.session.commit()
    return job

@pytest.fixture(scope='function')
def new_booking(new_user, new_job):
    booking = Booking(user_id=new_user.id, job_id=new_job.id, scheduled_time=datetime.utcnow() + timedelta(days=1))
    db.session.add(booking)
    db.session.commit()
    return booking
