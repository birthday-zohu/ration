from http.client import responses
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/ration', methods=['GET'])
def ration_proxy():
    try:
        # Get parameters
        aadhaar = request.args.get('aadhaar', '').strip()
        idtype = request.args.get('idtype', '').upper().strip()
        
        # Validate
        if not aadhaar or not idtype:
            return jsonify({
                'success': False,
                'message': 'aadhaar and idtype parameters required'
            }), 400
        
        if idtype not in ['R', 'U']:
            return jsonify({
                'success': False,
                'message': 'idtype must be R or U'
            }), 400
        
        # Make request to original API
        api_url = f"http://159.89.171.25:3000/search-aadhaar?aadhaar={aadhaar}&idtype={idtype}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json'
        }
        
        response = requests.get(api_url, headers=headers, timeout=10, verify=False)
        
        # Return the response
        return jsonify(response.json()), response.status_code
        
    except requests.exceptions.Timeout:
        return jsonify({
            'success': False,
            'message': 'Request timeout'
        }), 504
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'message': f'API Error: {str(e)}'
        }), 502
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Server Error: {str(e)}'
        }), 500

@app.route('/')
def home():
    return jsonify({
        'status': 'active',
        'service': 'Aadhaar API Proxy',
        'usage': '/api/ration?aadhaar=123456789012&idtype=U',
        'endpoints': {
            'ration_card': 'idtype=R',
            'aadhaar': 'idtype=U'
        }
    })

# For Vercel
if __name__ == '__main__':
    app.run(debug=True)
