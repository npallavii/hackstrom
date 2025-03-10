from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Server is running!'

@app.route('/api/book', methods=['POST'])
def book():
    data = request.get_json()
    print('Received:', data)
    return jsonify({
        'status': 'success',
        'message': 'Appointment booked!'
    })

print('Starting server on port 8080...')
app.run(host='localhost', port=8080, debug=True)
