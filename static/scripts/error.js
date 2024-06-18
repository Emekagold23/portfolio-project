document.addEventListener('DOMContentLoaded', function() {
    const backButton = document.getElementById('back-button');
    const homeButton = document.getElementById('home-button');

    backButton.addEventListener('click', function() {
        window.history.back();
    });

    homeButton.addEventListener('click', function() {
        window.location.href = '/';
    });
});