from flask import Blueprint, render_template, request, jsonify
from models import db, Review

review_routes = Blueprint('review_routes', __name__)

@review_routes.route('/reviews', methods=['GET'])
def reviews_page():
    return render_template('reviews.html')

@review_routes.route('/reviews', methods=['POST'])
def submit_review():
    data = request.json
    if not data.get('worker_id') or not data.get('rating') or not data.get('comment'):
        return jsonify({'error': 'Please provide worker_id, rating, and comment'}), 400
    
    new_review = Review(
        worker_id=data['worker_id'],
        rating=data['rating'],
        comment=data['comment']
    )
    db.session.add(new_review)
    db.session.commit()
    
    return jsonify({'message': 'Review submitted successfully'}), 201

@review_routes.route('/reviews/<int:worker_id>', methods=['GET'])
def get_worker_reviews(worker_id):
    reviews = Review.query.filter_by(worker_id=worker_id).all()
    reviews_data = [{
        'id': review.id,
        'worker_id': review.worker_id,
        'rating': review.rating,
        'comment': review.comment,
        'created_at': review.created_at
    } for review in reviews]
    
    return jsonify(reviews_data), 200
