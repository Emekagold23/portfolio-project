document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const form = document.querySelector('form');
    const titleInput = document.getElementById('title');
    const descriptionInput = document.getElementById('description');
    const dateInput = document.getElementById('date');
    const errorMessages = {
        title: 'Title is required',
        description: 'Description is required',
        date: 'Date is required'
    };

    form.addEventListener('submit', function(event) {
        let valid = true;
        const errors = [];

        if (!titleInput.value) {
            valid = false;
            errors.push(errorMessages.title);
        }

        if (!descriptionInput.value) {
            valid = false;
            errors.push(errorMessages.description);
        }

        if (!dateInput.value) {
            valid = false;
            errors.push(errorMessages.date);
        }

        if (!valid) {
            event.preventDefault();
            alert(errors.join('\n'));
        }
    });
});
