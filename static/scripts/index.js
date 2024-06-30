document.addEventListener('DOMContentLoaded', () => {
    console.log('Index page loaded');

    // Specific functionality for the homepage
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        heroSection.style.opacity = 0;
        setTimeout(() => {
            heroSection.style.transition = 'opacity 2s';
            heroSection.style.opacity = 1;
        }, 100);
    }

    // Testimonials carousel (if needed)
    const testimonials = document.querySelectorAll('.testimonial-item');
    let currentTestimonialIndex = 0;
    function showTestimonial(index) {
        testimonials.forEach((testimonial, i) => {
            testimonial.style.display = i === index ? 'block' : 'none';
        });
    }
    setInterval(() => {
        currentTestimonialIndex = (currentTestimonialIndex + 1) % testimonials.length;
        showTestimonial(currentTestimonialIndex);
    }, 5000);
});