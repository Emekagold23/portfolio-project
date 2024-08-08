document.addEventListener('DOMContentLoaded', () => {
    console.log('JS file loaded');

    const loginBtn = document.getElementById('login-btn');
    const signupBtn = document.getElementById('signup-btn');
    const loginPopup = document.getElementById('login-popup');
    const signupPopup = document.getElementById('signup-popup');
    const closeLoginPopup = document.getElementById('close-login-popup');
    const closeSignupPopup = document.getElementById('close-signup-popup');
    const signupWorkerBtn = document.getElementById('signup-worker');
    const signupClientBtn = document.getElementById('signup-client');

    loginBtn.addEventListener('click', () => {
        console.log('Login button clicked');
        loginPopup.style.display = 'flex';
    });

    signupBtn.addEventListener('click', () => {
        console.log('Signup button clicked');
        signupPopup.style.display = 'flex';
    });

    closeLoginPopup.addEventListener('click', () => {
        console.log('Close login popup button clicked');
        loginPopup.style.display = 'none';
    });

    closeSignupPopup.addEventListener('click', () => {
        console.log('Close signup popup button clicked');
        signupPopup.style.display = 'none';
    });

    signupWorkerBtn.addEventListener('click', () => {
        console.log('Signup as Worker button clicked');
        window.location.href = '/signup_worker';  // Update with your actual URL for worker signup
    });

    signupClientBtn.addEventListener('click', () => {
        console.log('Signup as Client button clicked');
        window.location.href = '/signup_client';  // Update with your actual URL for client signup
    });

    window.addEventListener('click', (e) => {
        if (e.target === loginPopup) {
            console.log('Click outside login popup');
            loginPopup.style.display = 'none';
        }
        if (e.target === signupPopup) {
            console.log('Click outside signup popup');
            signupPopup.style.display = 'none';
        }
    });
});
