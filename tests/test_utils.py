import pytest
from app.utils.auth import generate_token, verify_token, hash_password, check_password
from app.utils.validators import is_valid_email, is_valid_password

# Utility function for setting up
def setup_module(module):
    global token_secret_key
    token_secret_key = 'test_secret_key'

# Tests for auth utilities
def test_generate_token():
    payload = {'user_id': 1}
    token = generate_token(payload, secret_key=token_secret_key)
    assert isinstance(token, str)
    assert token != ''

def test_verify_token():
    payload = {'user_id': 1}
    token = generate_token(payload, secret_key=token_secret_key)
    verified_payload = verify_token(token, secret_key=token_secret_key)
    assert verified_payload['user_id'] == 1

def test_hash_password():
    password = 'securepassword'
    hashed = hash_password(password)
    assert hashed != password
    assert len(hashed) > 0

def test_check_password():
    password = 'securepassword'
    hashed = hash_password(password)
    assert check_password(password, hashed) is True
    assert check_password('wrongpassword', hashed) is False

# Tests for validators utilities
def test_is_valid_email():
    valid_email = "test@example.com"
    invalid_email = "test@example"
    assert is_valid_email(valid_email) is True
    assert is_valid_email(invalid_email) is False

def test_is_valid_password():
    valid_password = "StrongPass123!"
    invalid_password = "weak"
    assert is_valid_password(valid_password) is True
    assert is_valid_password(invalid_password) is False