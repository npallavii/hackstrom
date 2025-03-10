from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def serve_html():
    return send_from_directory('.', 'appointment.html')

@app.route('/api/book', methods=['POST'])
def book_appointment():
    data = request.json
    print('Received appointment:', data)  # Print to console for debugging
    
    return jsonify({
        'status': 'success',
        'message': 'Appointment booked successfully!'
    })

if __name__ == '__main__':
    app.run(port=3000, debug=True)
