document.addEventListener('DOMContentLoaded', function() {
    const servicesLink = document.querySelector('a[href="#hero"]');
    const contactLink = document.querySelector('a[href="#contact"]');

    servicesLink.addEventListener('click', function(event) {
        event.preventDefault();
        const servicesSection = document.getElementById('hero');
        servicesSection.scrollIntoView({ behavior: 'smooth' });
    });

    contactLink.addEventListener('click', function(event) {
        event.preventDefault();
        const contactSection = document.getElementById('contact');
        contactSection.scrollIntoView({ behavior: 'smooth' });
    });
});