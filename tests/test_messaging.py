import pytest
from models.message import send_message, get_conversation, list_user_conversations
from unittest.mock import patch, MagicMock

# Sample data for testing
message_data = {
    "sender_id": 1,
    "recipient_id": 2,
    "content": "Hello, this is a test message."
}

conversation_data = {
    "user1_id": 1,
    "user2_id": 2,
    "messages": [
        {"sender_id": 1, "recipient_id": 2, "content": "Hello, this is a test message."},
        {"sender_id": 2, "recipient_id": 1, "content": "Hi, received your message."}
    ]
}

user_conversations = [
    {"user_id": 1, "conversations": [conversation_data]}
]

# Mock Messaging Service
class MockMessagingService:
    def send(self, sender_id, recipient_id, content):
        return {"status": "success", "message": {"sender_id": sender_id, "recipient_id": recipient_id, "content": content}}

    def get_conversation(self, user1_id, user2_id):
        return {"status": "success", "conversation": conversation_data}

    def list_conversations(self, user_id):
        return {"status": "success", "conversations": user_conversations}

# Patch the messaging service in the messaging module
@patch('models.message.MessagingService', new=MockMessagingService)
def test_send_message():
    result = send_message(message_data["sender_id"], message_data["recipient_id"], message_data["content"])
    assert result["status"] == "success"
    assert result["message"]["sender_id"] == message_data["sender_id"]
    assert result["message"]["recipient_id"] == message_data["recipient_id"]
    assert result["message"]["content"] == message_data["content"]

@patch('models.message.MessagingService', new=MockMessagingService)
def test_get_conversation():
    result = get_conversation(conversation_data["user1_id"], conversation_data["user2_id"])
    assert result["status"] == "success"
    assert result["conversation"] == conversation_data

@patch('models.message.MessagingService', new=MockMessagingService)
def test_list_user_conversations():
    result = list_user_conversations(user_conversations[0]["user_id"])
    assert result["status"] == "success"
    assert result["conversations"] == user_conversations
