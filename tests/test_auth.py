import pytest
from models import User
from app import db

def test_register(client):
    response = client.post('/auth/register', json={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'password': 'password',
        'role': 'client'
    })
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Registered successfully'

def test_login(client, new_user):
    response = client.post('/auth/login', json={
        'email': new_user.email,
        'password': 'password'
    })
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Logged in successfully'

def test_logout(client, authenticated_user):
    response = client.get('/auth/logout')
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Logged out successfully'
