import pytest
from app.payments import process_payment, verify_payment, refund_payment
from unittest.mock import patch, MagicMock

# Sample data for testing
payment_data = {
    "user_id": 1,
    "amount": 100.00,
    "currency": "USD",
    "payment_method": "credit_card",
    "payment_details": {
        "card_number": "4111111111111111",
        "expiry_date": "12/24",
        "cvv": "123"
    }
}

payment_verification_data = {
    "payment_id": "payment123",
    "status": "success"
}

refund_data = {
    "payment_id": "payment123",
    "amount": 100.00
}

# Mock external payment gateway
class MockPaymentGateway:
    def process(self, payment_details):
        return {"status": "success", "payment_id": "payment123"}

    def verify(self, payment_id):
        return {"status": "success", "payment_id": payment_id}

    def refund(self, payment_id, amount):
        return {"status": "success", "payment_id": payment_id, "amount": amount}

# Patch the payment gateway in the payment module
@patch('app.payments.PaymentGateway', new=MockPaymentGateway)
def test_process_payment():
    result = process_payment(payment_data["user_id"], payment_data["amount"], payment_data["currency"], payment_data["payment_method"], payment_data["payment_details"])
    assert result["status"] == "success"
    assert result["payment_id"] == "payment123"

@patch('app.payments.PaymentGateway', new=MockPaymentGateway)
def test_verify_payment():
    result = verify_payment(payment_verification_data["payment_id"])
    assert result["status"] == "success"
    assert result["payment_id"] == payment_verification_data["payment_id"]

@patch('app.payments.PaymentGateway', new=MockPaymentGateway)
def test_refund_payment():
    result = refund_payment(refund_data["payment_id"], refund_data["amount"])
    assert result["status"] == "success"
    assert result["payment_id"] == refund_data["payment_id"]
    assert result["amount"] == refund_data["amount"]