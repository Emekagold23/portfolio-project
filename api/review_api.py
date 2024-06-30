from flask import Blueprint, request, jsonify
from utils.auth_utils import token_required
from services.review_service import ReviewService

review_api = Blueprint('review_api', __name__)

@review_api.route('/reviews', methods=['POST'])
@token_required
def create_review(user_id):
    data = request.get_json()
    if not data or 'job_id' not in data or 'rating' not in data:
        return jsonify({'error': 'Job ID and rating are required'}), 400
    review = ReviewService.create_review(user_id, data)
    if review:
        return jsonify(review), 201
    return jsonify({'error': 'Review could not be created'}), 500

@review_api.route('/reviews/<int:review_id>', methods=['GET'])
@token_required
def get_review(user_id, review_id):
    review = ReviewService.get_review(review_id)
    if review:
        return jsonify(review), 200
    return jsonify({'error': 'Review not found'}), 404

@review_api.route('/reviews/user/<int:user_id>', methods=['GET'])
@token_required
def get_reviews_by_user(user_id, target_user_id):
    reviews = ReviewService.get_reviews_by_user(target_user_id)
    if reviews:
        return jsonify(reviews), 200
    return jsonify({'error': 'No reviews found for this user'}), 404

@review_api.route('/reviews/job/<int:job_id>', methods=['GET'])
@token_required
def get_reviews_by_job(user_id, job_id):
    reviews = ReviewService.get_reviews_by_job(job_id)
    if reviews:
        return jsonify(reviews), 200
    return jsonify({'error': 'No reviews found for this job'}), 404

@review_api.route('/reviews/<int:review_id>', methods=['PUT'])
@token_required
def update_review(user_id, review_id):
    data = request.get_json()
    review = ReviewService.update_review(review_id, data)
    if review:
        return jsonify(review), 200
    return jsonify({'error': 'Review not found or could not be updated'}), 404

@review_api.route('/reviews/<int:review_id>', methods=['DELETE'])
@token_required
def delete_review(user_id, review_id):
    result = ReviewService.delete_review(review_id)
    if result:
        return jsonify({'message': 'Review deleted successfully'}), 200
    return jsonify({'error': 'Review not found'}), 404
