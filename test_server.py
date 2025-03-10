from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Server is working!'})

@app.route('/api/appointments', methods=['POST'])
def appointments():
    try:
        data = request.get_json()
        print('Received data:', data)
        return jsonify({
            'status': 'success',
            'message': 'Appointment booked successfully!'
        })
    except Exception as e:
        print('Error:', str(e))
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    print('Server starting on port 5000...')
    app.run(port=5000)
