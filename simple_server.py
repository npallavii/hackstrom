from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Server is working!'})

@app.route('/book', methods=['POST'])
def book():
    data = request.json
    print('Received:', data)
    return jsonify({'status': 'success', 'message': 'Appointment booked!'})

if __name__ == '__main__':
    print('Server starting on http://localhost:3000')
    app.run(port=3000)
