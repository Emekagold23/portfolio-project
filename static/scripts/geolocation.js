document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const form = document.querySelector('form');
    const nameInput = document.getElementById('name');
    const descriptionInput = document.getElementById('description');
    const latitudeInput = document.getElementById('latitude');
    const longitudeInput = document.getElementById('longitude');
    const errorMessages = {
        name: 'Name is required',
        description: 'Description is required',
        latitude: 'Latitude must be a valid number between -90 and 90',
        longitude: 'Longitude must be a valid number between -180 and 180',
    };

    form.addEventListener('submit', function(event) {
        let valid = true;
        const errors = [];

        if (!nameInput.value) {
            valid = false;
            errors.push(errorMessages.name);
        }

        if (!descriptionInput.value) {
            valid = false;
            errors.push(errorMessages.description);
        }

        const latitude = parseFloat(latitudeInput.value);
        if (isNaN(latitude) || latitude < -90 || latitude > 90) {
            valid = false;
            errors.push(errorMessages.latitude);
        }

        const longitude = parseFloat(longitudeInput.value);
        if (isNaN(longitude) || longitude < -180 || longitude > 180) {
            valid = false;
            errors.push(errorMessages.longitude);
        }

        if (!valid) {
            event.preventDefault();
            alert(errors.join('\n'));
        }
    });

    // Example interactive functionality (e.g., displaying current location)
    const currentLocationBtn = document.createElement('button');
    currentLocationBtn.textContent = 'Use Current Location';
    form.appendChild(currentLocationBtn);

    currentLocationBtn.addEventListener('click', function(event) {
        event.preventDefault();
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                latitudeInput.value = position.coords.latitude;
                longitudeInput.value = position.coords.longitude;
            }, function(error) {
                alert('Error retrieving current location: ' + error.message);
            });
        } else {
            alert('Geolocation is not supported by this browser.');
        }
    });
});
