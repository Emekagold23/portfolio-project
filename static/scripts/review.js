// JavaScript for Review pages

document.addEventListener('DOMContentLoaded', function () {
    console.log('Review script loaded');

    // Handle form submission for creating a new review
    const reviewForm = document.getElementById('create-review-form');
    if (reviewForm) {
        reviewForm.addEventListener('submit', function (event) {
            event.preventDefault();
            createReview();
        });
    }

    // Function to create a new review
    function createReview() {
        const rating = document.getElementById('rating').value;
        const comment = document.getElementById('comment').value;

        if (!rating || !comment) {
            alert('Please fill in all fields');
            return;
        }

        const reviewData = { rating, comment };

        fetch('/api/reviews', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(reviewData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Review submitted successfully');
                window.location.href = '/reviews';
            } else {
                alert('Failed to submit review');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Fetch and display reviews
    const reviewList = document.getElementById('review-list');
    if (reviewList) {
        fetch('/api/reviews')
            .then(response => response.json())
            .then(data => {
                data.forEach(review => {
                    const li = document.createElement('li');
                    li.textContent = `Rating: