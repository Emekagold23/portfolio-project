document.addEventListener('DOMContentLoaded', function() {
    // Payment form validation
    const paymentForm = document.querySelector('.create-payment form');
    if (paymentForm) {
        paymentForm.addEventListener('submit', function(event) {
            const title = document.getElementById('title').value.trim();
            const description = document.getElementById('description').value.trim();
            const amount = document.getElementById('amount').value.trim();
            const date = document.getElementById('date').value.trim();
            
            if (!title || !description || !amount || !date) {
                event.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    }

    // Payment list interactions
    const paymentListItems = document.querySelectorAll('.payments-list ul li a');
    if (paymentListItems) {
        paymentListItems.forEach(function(item) {
            item.addEventListener('click', function(event) {
                const confirmation = confirm('Do you want to view the details of this payment?');
                if (!confirmation) {
                    event.preventDefault();
                }
            });
        });
    }
});