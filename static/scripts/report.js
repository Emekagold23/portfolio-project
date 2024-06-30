document.addEventListener('DOMContentLoaded', function() {
    // Report form validation
    const reportForm = document.querySelector('.create-report form');
    if (reportForm) {
        reportForm.addEventListener('submit', function(event) {
            const title = document.getElementById('title').value.trim();
            const description = document.getElementById('description').value.trim();
            const date = document.getElementById('date').value.trim();
            
            if (!title || !description || !date) {
                event.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    }

    // Report list interactions
    const reportListItems = document.querySelectorAll('.reports ul li a');
    if (reportListItems) {
        reportListItems.forEach(function(item) {
            item.addEventListener('click', function(event) {
                const confirmation = confirm('Do you want to view the details of this report?');
                if (!confirmation) {
                    event.preventDefault();
                }
            });
        });
    }
});