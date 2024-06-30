import pytest
from flask import url_for

def test_home_page(test_client):
    response = test_client.get(url_for('home'))
    assert response.status_code == 200
    assert b"Home Page" in response.data

def test_user_login(test_client, init_database):
    response = test_client.post(url_for('auth.login'), data={
        'email': 'test@example.com',
        'password': 'FlaskIsAwesome'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Welcome" in response.data
