import pytest
from utils.email import send_email
from utils.token import generate_token, verify_token
from utils.helpers import format_date, get_current_time
from utils.validation import email_not_registered
from models import User
from datetime import datetime

def test_send_email(mocker):
    mocker.patch('utils.email.mail.send', return_value=True)
    result = send_email('test@example.com', 'Test Subject', 'Test Body')
    assert result is True

def test_generate_and_verify_token():
    token = generate_token(1)
    assert verify_token(token) == 1

def test_format_date():
    date = datetime(2021, 1, 1)
    assert format_date(date) == '2021-01-01'

def test_get_current_time():
    assert isinstance(get_current_time(), datetime)

def test_email_not_registered(mocker):
    mock_user = mocker.patch('models.User.query.filter_by')
    mock_user.return_value.first.return_value = None
    with pytest.raises(ValidationError):
        email_not_registered(None, type('', (), {'data': 'test@example.com'})())