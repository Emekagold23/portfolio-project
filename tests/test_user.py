import pytest
from app import db
from models import User

def test_new_user():
    user = User(first_name='John', last_name='Doe', email='john.doe@example.com', role='client')
    user.set_password('password123')
    
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.email == 'john.doe@example.com'
    assert user.role == 'client'
    assert user.check_password('password123')
    assert not user.check_password('wrongpassword')

def test_user_password_hashing():
    user = User(first_name='Jane', last_name='Doe', email='jane.doe@example.com', role='worker')
    user.set_password('mysecretpassword')
    
    assert user.password_hash != 'mysecretpassword'
    assert user.check_password('mysecretpassword')
    assert not user.check_password('wrongpassword')

def test_user_to_dict():
    user = User(first_name='Alice', last_name='Smith', email='alice.smith@example.com', role='client')
    user_dict = user.to_dict()
    
    assert user_dict['first_name'] == 'Alice'
    assert user_dict['last_name'] == 'Smith'
    assert user_dict['email'] == 'alice.smith@example.com'
    assert user_dict['role'] == 'client'

def test_user_repr():
    user = User(first_name='Bob', last_name='Brown', email='bob.brown@example.com', role='worker')
    
    assert repr(user) == '<User bob.brown@example.com>'
