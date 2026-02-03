from http.client import responses
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/ration', methods=['GET'])
def proxy():
    aadhaar = request.args.get('aadhaar', '')
    idtype = request.args.get('idtype', '')
    
    url = f"http://159.89.171.25:3000/search-aadhaar?aadhaar={aadhaar}&idtype={idtype}"
    
    try:
        response = requests.get(url, timeout=10)
        return response.text
    except:
        return '{"error": "API not working"}'

if __name__ == "__main__":
    app.run()
