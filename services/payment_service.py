from app import db
from models import Payment

class PaymentService:
    @staticmethod
    def create_payment(data):
        payment = Payment(**data)
        db.session.add(payment)
        db.session.commit()
        return payment.to_dict()

    @staticmethod
    def get_payment(payment_id):
        payment = Payment.query.get(payment_id)
        return payment.to_dict() if payment else None

    @staticmethod
    def get_payments_by_user(user_id):
        payments = Payment.query.filter_by(user_id=user_id).all()
        return [payment.to_dict() for payment in payments] if payments else []
