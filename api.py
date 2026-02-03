from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# U type के लिए
@app.route('/api/aadhaar', methods=['GET'])
def aadhaar_api():
    aadhaar = request.args.get('aadhaar', '')
    
    if not aadhaar:
        return jsonify({
            'success': False,
            'error': 'AADHAAR_REQUIRED',
            'message': 'Aadhaar number is required'
        }), 400
    
    url = f"http://159.89.171.25:3000/search-aadhaar?aadhaar={aadhaar}&idtype=U"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        return jsonify({
            'success': True,
            'type': 'AADHAAR',
            'aadhaar': aadhaar,
            'data': data,
            'timestamp': '2024-01-01T00:00:00Z'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'API_ERROR',
            'message': str(e),
            'type': 'AADHAAR'
        }), 500

# R type के लिए
@app.route('/api/ration', methods=['GET'])
def ration_api():
    aadhaar = request.args.get('aadhaar', '')
    
    if not aadhaar:
        return jsonify({
            'success': False,
            'error': 'AADHAAR_REQUIRED',
            'message': 'Aadhaar number is required'
        }), 400
    
    url = f"http://159.89.171.25:3000/search-aadhaar?aadhaar={aadhaar}&idtype=R"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        return jsonify({
            'success': True,
            'type': 'RATION',
            'aadhaar': aadhaar,
            'data': data,
            'timestamp': '2024-01-01T00:00:00Z'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'API_ERROR',
            'message': str(e),
            'type': 'RATION'
        }), 500

@app.route('/')
def home():
    return jsonify({
        'success': True,
        'apis': {
            'aadhaar': '/api/aadhaar?aadhaar=123456789012',
            'ration': '/api/ration?aadhaar=123456789012'
        }
    })

if __name__ == '__main__':
    app.run()
