import pytest
from models.notification import send_notification
from unittest.mock import patch, MagicMock

# Mock Notification Service
class MockNotificationService:
    def send_notification(self, user_id, message):
        return {"status": "success", "message": "Notification sent successfully"}

# Patch the notification service in the notifications module
@patch('models.notification.NotificationService', new=MockNotificationService)
def test_send_notification():
    result = send_notification(1, "Your booking has been confirmed.")
    assert result["status"] == "success"
    assert result["message"] == "Notification sent successfully"
