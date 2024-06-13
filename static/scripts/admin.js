// JavaScript for Admin pages

document.addEventListener('DOMContentLoaded', function () {
    console.log('Admin script loaded');

    // Handle form submission for creating a new user by admin
    const adminForm = document.getElementById('create-user-form');
    if (adminForm) {
        adminForm.addEventListener('submit', function (event) {
            event.preventDefault();
            createUser();
        });
    }

    // Function to create a new user
    function createUser() {
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        if (!name || !email || !password) {
            alert('Please fill in all fields');
            return;
        }

        const userData = { name, email, password };

        fetch('/api/users', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(userData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('User created successfully');
                window.location.href = '/admin/users';
            } else {
                alert('Failed to create user');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Fetch and display users
    const userList = document.getElementById('user-list');
    if (userList) {
        fetch('/api/users')
            .then(response => response.json())
            .then(data => {
                data.forEach(user => {
                    const li = document.createElement('li');
                    li.textContent = `Name: ${user.name}, Email: ${user.email}`;
                    userList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }
});
