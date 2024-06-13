document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript loaded successfully!');

    // Handle form submission for creating a new booking
    const bookingForm = document.querySelector('form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission
            createBooking();
        });
    }

    // Function to create a new booking
    function createBooking() {
        const userId = document.getElementById('user_id').value;
        const jobId = document.getElementById('job_id').value;
        const scheduledTime = document.getElementById('scheduled_time').value;

        if (!userId || !jobId || !scheduledTime) {
            alert('Please fill in all fields');
            return;
        }

        const bookingData = {
            user_id: userId,
            job_id: jobId,
            scheduled_time: scheduledTime
        };

        fetch('/api/bookings', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(bookingData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.message === 'Booking created successfully') {
                alert('Booking created successfully');
                window.location.href = '/bookings'; // Redirect to bookings page
            } else {
                alert('Failed to create booking');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Fetch and display bookings
    const bookingList = document.getElementById('booking-list');
    if (bookingList) {
        fetch('/api/bookings')
            .then(response => response.json())
            .then(data => {
                data.forEach(booking => {
                    const li = document.createElement('li');
                    li.textContent = `Job ID: ${booking.job_id}, Scheduled Time: ${booking.scheduled_time}`;
                    bookingList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});





// JavaScript for Booking pages

document.addEventListener('DOMContentLoaded', function () {
    console.log('Booking script loaded');

    // Handle form submission for creating a new booking
    const bookingForm = document.getElementById('create-booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function (event) {
            event.preventDefault();
            createBooking();
        });
    }

    // Function to create a new booking
    function createBooking() {
        const userId = document.getElementById('user_id').value;
        const jobId = document.getElementById('job_id').value;
        const scheduledTime = document.getElementById('scheduled_time').value;

        if (!userId || !jobId || !scheduledTime) {
            alert('Please fill in all fields');
            return;
        }

        const bookingData = { user_id: userId, job_id: jobId, scheduled_time: scheduledTime };

        fetch('/api/bookings', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(bookingData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Booking created successfully');
                window.location.href = '/bookings';
            } else {
                alert('Failed to create booking');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Fetch and display bookings
    const bookingList = document.getElementById('booking-list');
    if (bookingList) {
        fetch('/api/bookings')
            .then(response => response.json())
            .then(data => {
                data.forEach(booking => {
                    const li = document.createElement('li');
                    li.textContent = `Job ID: ${booking.job_id}, Scheduled Time: ${booking.scheduled_time}`;
                    bookingList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});