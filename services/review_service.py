from app import db
from models import Review

class ReviewService:
    @staticmethod
    def create_review(user_id, data):
        new_review = Review(
            user_id=user_id,
            job_id=data['job_id'],
            rating=data['rating'],
            comment=data.get('comment', '')
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review.to_dict()

    @staticmethod
    def get_review(review_id):
        review = Review.query.get(review_id)
        if review:
            return review.to_dict()
        return None

    @staticmethod
    def get_reviews_by_user(user_id):
        reviews = Review.query.filter_by(user_id=user_id).all()
        return [review.to_dict() for review in reviews]

    @staticmethod
    def get_reviews_by_job(job_id):
        reviews = Review.query.filter_by(job_id=job_id).all()
        return [review.to_dict() for review in reviews]

    @staticmethod
    def update_review(review_id, data):
        review = Review.query.get(review_id)
        if review:
            review.rating = data.get('rating', review.rating)
            review.comment = data.get('comment', review.comment)
            db.session.commit()
            return review.to_dict()
        return None

    @staticmethod
    def delete_review(review_id):
        review = Review.query.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        return False
