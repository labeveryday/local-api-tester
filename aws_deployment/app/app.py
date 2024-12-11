from flask import Flask, request, jsonify
from flask_lambda import FlaskLambda
import requests
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FlaskLambda(__name__)  # Use FlaskLambda for AWS Lambda compatibility


@app.route('/')
def index():
    return jsonify({"message": "Welcome to API Tester!"})

@app.route('/make_request', methods=['POST'])
def make_request():
    url = request.json.get('url')
    method = request.json.get('method', 'GET').upper()
    headers = request.json.get('headers', {})
    body = request.json.get('body', '')
    logger.info(f"Received request: URL={url}, Method={method}, Headers={headers}, Body={body}")

    try:
        # Make HTTP requests based on the method
        if method not in ['GET', 'POST']:
            return jsonify({"error": "HTTP method not allowed"}), 405
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=body)
        else:
            return jsonify({'error': 'Unsupported method'}), 400
        
        response = {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response.text
        }

        logger.info(f"Response: {json.dumps(response)}")

        return jsonify(response)
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
