import pytest
from app.reviews import add_review, get_worker_reviews
from unittest.mock import patch, MagicMock

# Mock Review Service
class MockReviewService:
    def add_review(self, user_id, worker_id, rating, comment):
        return {"status": "success", "message": "Review added successfully"}

    def get_worker_reviews(self, worker_id):
        return {"status": "success", "reviews": [{"user_id": 1, "rating": 5, "comment": "Great service!"}]}

# Patch the review service in the reviews module
@patch('app.reviews.ReviewService', new=MockReviewService)
def test_add_review():
    result = add_review(1, 2, 5, "Great service!")
    assert result["status"] == "success"
    assert result["message"] == "Review added successfully"

@patch('app.reviews.ReviewService', new=MockReviewService)
def test_get_worker_reviews():
    worker_id = 2
    result = get_worker_reviews(worker_id)
    assert result["status"] == "success"
    assert len(result["reviews"]) == 1