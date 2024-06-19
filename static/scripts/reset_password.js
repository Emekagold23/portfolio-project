document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const formData = new FormData(form);
        const email = formData.get('email');

        try {
            const response = await fetch('/reset-password', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email })
            });

            if (!response.ok) {
                throw new Error('Password reset request failed');
            }

            // Handle successful password reset request
            alert('Password reset link sent to your email.'); // Example message
        } catch (error) {
            console.error('Error resetting password:', error);
            // Handle error (e.g., display error message)
        }
    });
});