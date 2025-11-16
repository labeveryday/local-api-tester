from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/make_request', methods=['POST'])
def make_request():
    url = request.form['url']
    method = request.form['method']
    headers_str = request.form.get('headers', '{}')
    body = request.form.get('body', '')

    # Parse headers from JSON string
    try:
        headers = json.loads(headers_str) if headers_str else {}
    except json.JSONDecodeError:
        headers = {}

    try:
        # 30 second timeout to prevent hanging on unresponsive endpoints
        timeout = 30

        if method == 'GET':
            response = requests.get(url, headers=headers, timeout=timeout)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=body, timeout=timeout)
        elif method == 'PUT':
            response = requests.put(url, headers=headers, data=body, timeout=timeout)
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers, timeout=timeout)
        elif method == 'PATCH':
            response = requests.patch(url, headers=headers, data=body, timeout=timeout)
        else:
            return jsonify({'error': 'Unsupported method'})

        return jsonify({
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response.text
        })
    except requests.RequestException as e:
        return jsonify({'error': str(e), 'status_code': 500})


if __name__ == '__main__':
    # Bind to localhost only - NOT accessible from outside network
    # debug=True is acceptable for local development only (never deploy to production with debug=True)
    app.run(host='127.0.0.1', port=5000, debug=True)  # nosec B201
