document.addEventListener('DOMContentLoaded', function() {
    // Notification list interactions
    const notificationListItems = document.querySelectorAll('.notification-list li');
    if (notificationListItems) {
        notificationListItems.forEach(function(item) {
            item.addEventListener('click', function() {
                alert('Notification clicked: ' + item.querySelector('.notification-message').textContent);
            });
        });
    }
});