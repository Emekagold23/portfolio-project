import pytest
from app.admin import get_users, get_jobs
from unittest.mock import patch, MagicMock

# Mock Admin Service
class MockAdminService:
    def get_users(self):
        return {"status": "success", "users": [{"id": 1, "username": "admin", "role": "admin"}]}

    def get_jobs(self):
        return {"status": "success", "jobs": [{"id": 1, "title": "Plumbing", "status": "pending"}]}

# Patch the admin service in the admin module
@patch('app.admin.AdminService', new=MockAdminService)
def test_get_users():
    result = get_users()
    assert result["status"] == "success"
    assert len(result["users"]) == 1

@patch('app.admin.AdminService', new=MockAdminService)
def test_get_jobs():
    result = get_jobs()
    assert result["status"] == "success"
    assert len(result["jobs"]) == 1