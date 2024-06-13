// JavaScript for Payment pages

document.addEventListener('DOMContentLoaded', function () {
    console.log('Payment script loaded');

    // Handle form submission for creating a new payment
    const paymentForm = document.getElementById('create-payment-form');
    if (paymentForm) {
        paymentForm.addEventListener('submit', function (event) {
            event.preventDefault();
            createPayment();
        });
    }

    // Function to create a new payment
    function createPayment() {
        const amount = document.getElementById('amount').value;
        const method = document.getElementById('method').value;

        if (!amount || !method) {
            alert('Please fill in all fields');
            return;
        }

        const paymentData = { amount, method };

        fetch('/api/payments', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(paymentData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Payment created successfully');
                window.location.href = '/payments';
            } else {
                alert('Failed to create payment');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Fetch and display payments
    const paymentList = document.getElementById('payment-list');
    if (paymentList) {
        fetch('/api/payments')
            .then(response => response.json())
            .then(data => {
                data.forEach(payment => {
                    const li = document.createElement('li');
                    li.textContent = `Amount: ${payment.amount}, Method: ${payment.method}`;
                    paymentList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});