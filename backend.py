from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    try:
        data = request.get_json()
        print("Received data:", data)  # Console logging
        return jsonify({
            'status': 'success',
            'message': 'Appointment request received',
            'data': data
        })
    except Exception as e:
        print("Error:", str(e))  # Console logging
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
