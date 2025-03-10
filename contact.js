document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();

            const formData = {
                name: document.getElementById('name').value.trim(),
                email: document.getElementById('email').value.trim(),
                phone: document.getElementById('phone').value.trim(),
                department: document.getElementById('department').value.trim(),
                message: document.getElementById('message').value.trim()
            };

            try {
                const response = await fetch('http://localhost:5001/api/contact', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                const data = await response.json();
                
                if (data.status === 'success') {
                    alert(data.message);
                    contactForm.reset();
                } else {
                    alert('Error: ' + (data.message || 'Failed to send message'));
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Failed to connect to server. Please try again later.');
            }
        });
    }
});
