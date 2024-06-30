// JavaScript for User Authentication and Profile pages

document.addEventListener('DOMContentLoaded', function () {
    console.log('User script loaded');

    // Handle form submission for login
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function (event) {
            event.preventDefault();
            loginUser();
        });
    }

    // Function to login a user
    function loginUser() {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        if (!email || !password) {
            alert('Please fill in all fields');
            return;
        }

        const loginData = { email, password };

        fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(loginData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.token) {
                // Store token in local storage or cookie
                localStorage.setItem('token', data.token);
                alert('Login successful');
                window.location.href = '/profile';
            } else {
                alert('Failed to login: ' + (data.message || 'Unknown error'));
            }
        })
        .catch(error => console.error('Error:', error));
    }

    // Function to handle form submission for profile update
    const profileForm = document.getElementById('profile-form');
    if (profileForm) {
        profileForm.addEventListener('submit', function (event) {
            event.preventDefault();
            updateProfile();
        });
    }

    // Function to update the user profile
    function updateProfile() {
        const token = localStorage.getItem('token');
        if (!token) {
            alert('User not logged in');
            return;
        }

        const firstName = document.getElementById('first_name').value;
        const lastName = document.getElementById('last_name').value;
        const email = document.getElementById('email').value;

        const profileData = { first_name: firstName, last_name: lastName, email: email };

        fetch('/api/profile', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify(profileData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Profile updated successfully');
                window.location.reload();
            } else {
                alert('Failed to update profile: ' + (data.message || 'Unknown error'));
            }
        })
        .catch(error => console.error('Error:', error));
    }
});