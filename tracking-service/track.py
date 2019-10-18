from flask import request
from flask import Response
from flask import Flask
app = Flask(__name__)

@app.route('/api/v2/cache/', methods=['GET', 'POST','OPTIONS'])
def upload_file():
    if request.method == 'POST':
        payload = request.data
        with open('/tmp/tracking.txt', 'a') as f:
            f.write(str(payload) + "\n")
        resp = Response('', status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://localhost'
        return resp
    if request.method == 'GET' or request.method == 'OPTIONS':
        with open('./ff.json', 'r') as f:
            featureFlag = f.read()
        resp = Response(featureFlag, status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://localhost'
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp
    else:
        return "hmm let's see"
