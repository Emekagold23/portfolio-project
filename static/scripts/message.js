// JavaScript for Messaging pages

document.addEventListener('DOMContentLoaded', function () {
    console.log('Message script loaded');

    // Handle form submission for creating a new message
    const messageForm = document.getElementById('create-message-form');
    if (messageForm) {
        messageForm.addEventListener('submit', function (event) {
            event.preventDefault();
            createMessage();
        });
    }

    // Function to create a new message
    function createMessage() {
        const recipient = document.getElementById('recipient').value;
        const content = document.getElementById('content').value;

        if (!recipient || !content) {
            alert('Please fill in all fields');
            return;
        }

        const messageData = { recipient, content };

        fetch('/api/messages', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(messageData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Message sent successfully');
                window.location.href = '/messages';
            } else {
                alert('Failed to send message');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Fetch and display messages
    const messageList = document.getElementById('message-list');
    if (messageList) {
        fetch('/api/messages')
            .then(response => response.json())
            .then(data => {
                data.forEach(message => {
                    const li = document.createElement('li');
                    li.textContent = `To: ${message.recipient}, Content: ${message.content}`;
                    messageList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});