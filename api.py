from flask import Flask, request
import requests

app = Flask(__name__)

# U type के लिए
@app.route('/api/aadhaar', methods=['GET'])
def aadhaar_api():
    aadhaar = request.args.get('aadhaar', '')
    
    if not aadhaar:
        return '{"error": "aadhaar required"}', 400
    
    url = f"http://159.89.171.25:3000/search-aadhaar?aadhaar={aadhaar}&idtype=U"
    
    try:
        response = requests.get(url, timeout=10)
        return response.text, response.status_code, {'Content-Type': 'application/json'}
    except:
        return '{"error": "api error"}', 500

# R type के लिए  
@app.route('/api/ration', methods=['GET'])
def ration_api():
    aadhaar = request.args.get('aadhaar', '')
    
    if not aadhaar:
        return '{"error": "aadhaar required"}', 400
    
    url = f"http://159.89.171.25:3000/search-aadhaar?aadhaar={aadhaar}&idtype=R"
    
    try:
        response = requests.get(url, timeout=10)
        return response.text, response.status_code, {'Content-Type': 'application/json'}
    except:
        return '{"error": "api error"}', 500

@app.route('/')
def home():
    return '{"apis": ["/api/aadhaar", "/api/ration"]}'

if __name__ == '__main__':
    app.run()
