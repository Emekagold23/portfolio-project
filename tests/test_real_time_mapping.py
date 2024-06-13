import pytest
from app.real_time_mapping import update_location, get_user_location, notify_nearby_users
from unittest.mock import patch

# Sample data for testing
user_location_data = {
    "user_id": 1,
    "latitude": 40.7128,
    "longitude": -74.0060
}

nearby_users_data = [
    {"user_id": 2, "latitude": 40.7127, "longitude": -74.0059},
    {"user_id": 3, "latitude": 40.7129, "longitude": -74.0061},
]

# Mock database or cache
user_locations = {}

# Mock functions for database/cache interactions
def mock_save_location(user_id, latitude, longitude):
    user_locations[user_id] = {"latitude": latitude, "longitude": longitude}

def mock_get_location(user_id):
    return user_locations.get(user_id)

# Tests for update_location function
@patch('app.real_time_mapping.save_location', side_effect=mock_save_location)
def test_update_location(mock_save):
    user_id = user_location_data["user_id"]
    latitude = user_location_data["latitude"]
    longitude = user_location_data["longitude"]

    update_location(user_id, latitude, longitude)
    
    assert user_locations[user_id]["latitude"] == latitude
    assert user_locations[user_id]["longitude"] == longitude

# Tests for get_user_location function
@patch('app.real_time_mapping.get_location', side_effect=mock_get_location)
def test_get_user_location(mock_get):
    user_id = user_location_data["user_id"]
    user_locations[user_id] = {"latitude": user_location_data["latitude"], "longitude": user_location_data["longitude"]}
    
    location = get_user_location(user_id)
    
    assert location["latitude"] == user_location_data["latitude"]
    assert location["longitude"] == user_location_data["longitude"]

# Mock function for notifying nearby users
def mock_notify(users, message):
    # Just a placeholder for testing purposes
    return True

# Tests for notify_nearby_users function
@patch('app.real_time_mapping.notify', side_effect=mock_notify)
@patch('app.real_time_mapping.get_nearby_users', return_value=nearby_users_data)
def test_notify_nearby_users(mock_nearby, mock_notify):
    user_id = user_location_data["user_id"]
    latitude = user_location_data["latitude"]
    longitude = user_location_data["longitude"]
    message = "New user nearby!"
    
    result = notify_nearby_users(user_id, latitude, longitude, message)
    
    assert result is True
    mock_notify.assert_called_once_with(nearby_users_data, message)
    mock_nearby.assert_called_once_with(latitude, longitude)