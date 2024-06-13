from models import User, Job, Review, Booking
from sqlalchemy import or_

class SearchService:
    @staticmethod
    def search(query):
        if not query:
            return []

        query = f"%{query}%"
        users = User.query.filter(or_(
            User.username.ilike(query),
            User.email.ilike(query),
            User.first_name.ilike(query),
            User.last_name.ilike(query)
        )).all()

        jobs = Job.query.filter(or_(
            Job.title.ilike(query),
            Job.description.ilike(query)
        )).all()

        reviews = Review.query.filter(or_(
            Review.comment.ilike(query)
        )).all()

        bookings = Booking.query.filter(or_(
            Booking.scheduled_time.ilike(query)
        )).all()

        results = {
            'users': [user.to_dict() for user in users],
            'jobs': [job.to_dict() for job in jobs],
            'reviews': [review.to_dict() for review in reviews],
            'bookings': [booking.to_dict() for booking in bookings],
        }
        return results