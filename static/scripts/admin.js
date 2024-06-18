document.addEventListener('DOMContentLoaded', function() {
    // Event listener for delete buttons in job and report lists
    const deleteButtons = document.querySelectorAll('form button[type="submit"]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            if (!confirm('Are you sure you want to delete this item?')) {
                event.preventDefault();
            }
        });
    });
});