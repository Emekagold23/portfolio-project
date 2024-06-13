from flask import Blueprint, render_template, request, redirect, url_for
from models import Payment, db

payment_routes = Blueprint('payment_routes', __name__)

@payment_routes.route('/payments', methods=['GET'])
def payments_page():
    payments = Payment.query.all()
    return render_template('payments.html', payments=payments)

@payment_routes.route('/payments/<int:payment_id>', methods=['GET'])
def payment_page(payment_id):
    payment = Payment.query.get_or_404(payment_id)
    return render_template('payment.html', payment=payment)

@payment_routes.route('/payments/create', methods=['GET', 'POST'])
def create_payment_page():
    if request.method == 'POST':
        data = request.form
        new_payment = Payment(
            user_id=data['user_id'],
            amount=data['amount'],
            method=data['method']
        )
        db.session.add(new_payment)
        db.session.commit()
        return redirect(url_for('payment_routes.payments_page'))
    return render_template('create_payment.html')
