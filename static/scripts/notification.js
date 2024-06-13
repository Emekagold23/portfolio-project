// JavaScript for Notification services

document.addEventListener('DOMContentLoaded', function () {
    console.log('Notification script loaded');

    // Handle form submission for creating a new notification
    const notificationForm = document.getElementById('create-notification-form');
    if (notificationForm) {
        notificationForm.addEventListener('submit', function (event) {
            event.preventDefault();
            createNotification();
        });
    }

    // Function to create a new notification
    function createNotification() {
        const title = document.getElementById('title').value;
        const message = document.getElementById('message').value;

        if (!title || !message) {
            alert('Please fill in all fields');
            return;
        }

        const notificationData = { title, message };

        fetch('/api/notifications', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(notificationData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Notification created successfully');
                window.location.href = '/notifications';
            } else {
                alert('Failed to create notification');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Fetch and display notifications
    const notificationList = document.getElementById('notification-list');
    if (notificationList) {
        fetch('/api/notifications')
            .then(response => response.json())
            .then(data => {
                data.forEach(notification => {
                    const li = document.createElement('li');
                    li.textContent = `Title: ${notification.title}, Message: ${notification.message}`;
                    notificationList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});
