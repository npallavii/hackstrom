from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from flask_mail import Mail, Message
import os

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-password'  # Replace with your email password

db = SQLAlchemy(app)
mail = Mail(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    doctor = db.Column(db.String(100))
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(10), nullable=False)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'department': self.department,
            'doctor': self.doctor,
            'date': self.date.strftime('%Y-%m-%d'),
            'time': self.time,
            'message': self.message,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

def send_confirmation_email(appointment):
    msg = Message('Appointment Confirmation',
                sender=app.config['MAIL_USERNAME'],
                recipients=[appointment.email])
    
    msg.body = f'''Dear {appointment.name},

Your appointment has been successfully scheduled:

Date: {appointment.date}
Time: {appointment.time}
Department: {appointment.department}
Doctor: {appointment.doctor if appointment.doctor else "To be assigned"}

Please arrive 15 minutes before your appointment time.
Don't forget to bring:
- Your ID
- Insurance card
- Medical records
- List of current medications

If you need to cancel or reschedule, please contact us at least 24 hours in advance.

Best regards,
HealthCare Hospital Team'''
    
    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    try:
        data = request.json
        
        # Convert date string to date object
        appointment_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        
        # Create new appointment
        new_appointment = Appointment(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            department=data['department'],
            doctor=data.get('doctor', ''),
            date=appointment_date,
            time=data['time'],
            message=data.get('message', '')
        )
        
        # Save to database
        db.session.add(new_appointment)
        db.session.commit()
        
        # Send confirmation email
        send_confirmation_email(new_appointment)
        
        return jsonify({
            'status': 'success',
            'message': 'Appointment booked successfully',
            'appointment': new_appointment.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    appointments = Appointment.query.all()
    return jsonify({
        'status': 'success',
        'appointments': [appointment.to_dict() for appointment in appointments]
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
