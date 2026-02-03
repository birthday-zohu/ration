from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API 1: UID के लिए (idtype=U)
@app.route('/api/ration', methods=['GET'])
def uid_proxy():
    aadhaar = request.args.get('aadhaar', '')
    idtype = request.args.get('idtype', 'U')  # Default U
    
    if not aadhaar:
        return jsonify({'error': 'Aadhaar number required'}), 400
    
    url = f"http://159.89.171.25:3000/search-aadhaar?aadhaar={aadhaar}&idtype={idtype}"
    
    try:
        response = requests.get(url, timeout=10)
        return response.text, response.status_code
    except:
        return jsonify({'error': 'API server error'}), 500

# API 2: Ration के लिए (idtype=R)  
@app.route('/api/ration-card', methods=['GET'])
def ration_proxy():
    aadhaar = request.args.get('aadhaar', '')
    idtype = 'R'  # Always R for ration
    
    if not aadhaar:
        return jsonify({'error': 'Aadhaar number required'}), 400
    
    url = f"http://159.89.171.25:3000/search-aadhaar?aadhaar={aadhaar}&idtype={idtype}"
    
    try:
        response = requests.get(url, timeout=10)
        return response.text, response.status_code
    except:
        return jsonify({'error': 'API server error'}), 500

# Single endpoint for both
@app.route('/api/search', methods=['GET'])
def search():
    aadhaar = request.args.get('aadhaar', '')
    idtype = request.args.get('idtype', 'U')  # Default U
    
    if not aadhaar:
        return jsonify({'error': 'Aadhaar number required'}), 400
    
    if idtype not in ['R', 'U']:
        return jsonify({'error': 'idtype must be R or U'}), 400
    
    url = f"http://159.89.171.25:3000/search-aadhaar?aadhaar={aadhaar}&idtype={idtype}"
    
    try:
        response = requests.get(url, timeout=10)
        return response.text, response.status_code
    except:
        return jsonify({'error': 'API server error'}), 500

@app.route('/')
def home():
    return jsonify({
        'message': 'Aadhaar & Ration Card API Proxy',
        'endpoints': {
            '/api/ration': 'UID/Aadhaar Search (idtype=U)',
            '/api/ration-card': 'Ration Card Search (idtype=R)',
            '/api/search': 'Both (specify idtype=R/U)'
        },
        'example': '/api/ration?aadhaar=123456789012'
    })

if __name__ == '__main__':
    app.run()
