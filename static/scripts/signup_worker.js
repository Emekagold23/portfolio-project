document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const formData = new FormData(form);
        const firstName = formData.get('first_name');
        const lastName = formData.get('last_name');
        const email = formData.get('email');
        const password = formData.get('password');
        const confirmPassword = formData.get('confirm_password');
        const services = formData.get('services');
        const availability = formData.get('availability');

        if (password !== confirmPassword) {
            // Handle password mismatch error (e.g., display error message)
            return;
        }

        try {
            const response = await fetch('/signup/worker', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ firstName, lastName, email, password, services, availability })
            });

            if (!response.ok) {
                throw new Error('Signup failed');
            }

            // Redirect or handle successful signup
            window.location.href = '/dashboard'; // Example redirect
        } catch (error) {
            console.error('Error signing up:', error);
            // Handle error (e.g., display error message)
        }
    });
});
