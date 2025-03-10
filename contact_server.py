from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        logger.info(f"Received contact form submission: {data}")
        
        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'department', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'status': 'error',
                    'message': f'Missing required field: {field}'
                }), 400

        # Here you would typically save to database or send email
        # For now, we'll just log it
        logger.info("Contact form data validated successfully")
        
        return jsonify({
            'status': 'success',
            'message': 'Thank you for contacting us! We will get back to you soon.'
        })

    except Exception as e:
        logger.error(f"Error processing contact form: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'An error occurred while processing your request'
        }), 500

if __name__ == '__main__':
    print('Contact form server starting on port 5001...')
    app.run(host='localhost', port=5001, debug=True)
