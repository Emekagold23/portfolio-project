document.addEventListener('DOMContentLoaded', function() {
    // Booking form validation
    const bookingForm = document.querySelector('.create-booking form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(event) {
            const title = document.getElementById('title').value.trim();
            const description = document.getElementById('description').value.trim();
            const date = document.getElementById('date').value.trim();
            
            if (!title || !description || !date) {
                event.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    }

    // Booking list interactions
    const bookingListItems = document.querySelectorAll('.bookings ul li a');
    if (bookingListItems) {
        bookingListItems.forEach(function(item) {
            item.addEventListener('click', function(event) {
                const confirmation = confirm('Do you want to view the details of this booking?');
                if (!confirmation) {
                    event.preventDefault();
                }
            });
        });
    }
});