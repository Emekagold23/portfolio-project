// JavaScript for Geolocation services

document.addEventListener('DOMContentLoaded', function () {
    console.log('Geolocation script loaded');

    // Handle geolocation requests
    const geolocationButton = document.getElementById('get-location');
    if (geolocationButton) {
        geolocationButton.addEventListener('click', function () {
            getGeolocation();
        });
    }

    // Function to get the user's geolocation
    function getGeolocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            alert('Geolocation is not supported by this browser.');
        }
    }

    function showPosition(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        alert(`Latitude: ${lat}, Longitude: ${lon}`);
    }

    function showError(error) {
        switch (error.code) {
            case error.PERMISSION_DENIED:
                alert('User denied the request for Geolocation.');
                break;
            case error.POSITION_UNAVAILABLE:
                alert('Location information is unavailable.');
                break;
            case error.TIMEOUT:
                alert('The request to get user location timed out.');
                break;
            case error.UNKNOWN_ERROR:
                alert('An unknown error occurred.');
                break;
        }
    }
});