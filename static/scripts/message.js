document.addEventListener('DOMContentLoaded', function() {
    // Message list interactions
    const messageListItems = document.querySelectorAll('.message-list li a');
    if (messageListItems) {
        messageListItems.forEach(function(item) {
            item.addEventListener('click', function(event) {
                event.preventDefault();
                const messageUrl = item.getAttribute('href');
                // Fetch and display the message details
                fetch(messageUrl)
                    .then(response => response.text())
                    .then(data => {
                        document.querySelector('main').innerHTML = data;
                    })
                    .catch(error => console.error('Error fetching message:', error));
            });
        });
    }
});