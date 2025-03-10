document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('appointmentForm');
    
    // Set minimum date to today
    const dateInput = document.getElementById('date');
    const today = new Date().toISOString().split('T')[0];
    dateInput.min = today;

    // Handle department selection
    const departmentSelect = document.getElementById('department');
    const doctorSelect = document.getElementById('doctor');
    
    departmentSelect.addEventListener('change', function() {
        const dept = this.value;
        const doctors = {
            'cardiology': 'Dr. Sarah Johnson',
            'neurology': 'Dr. Michael Chen',
            'orthopedics': 'Dr. Emily Williams',
            'general-medicine': 'Dr. David Kumar'
        };
        
        doctorSelect.innerHTML = '<option value="">Select Doctor</option>';
        if (doctors[dept]) {
            doctorSelect.innerHTML += `<option value="${doctors[dept]}">${doctors[dept]}</option>`;
        }
    });

    // Handle form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            department: document.getElementById('department').value,
            doctor: document.getElementById('doctor').value,
            date: document.getElementById('date').value,
            time: document.getElementById('time').value,
            message: document.getElementById('message').value
        };

        try {
            const response = await fetch('http://localhost:8080/api/book', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();
            if (result.status === 'success') {
                alert('Appointment booked successfully!');
                form.reset();
            } else {
                alert('Error booking appointment');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Server connection error. Please make sure the server is running.');
        }
    });
});
