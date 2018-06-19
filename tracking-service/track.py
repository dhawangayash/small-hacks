from flask import request
from flask import Response
from flask import Flask
app = Flask(__name__)

@app.route('/track', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        payload = request.data
        with open('/tmp/tracking.txt', 'a') as f:
            f.write(str(payload) + "\n")
        resp = Response('', status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://localhost'
        return resp
    else:
        return "hmm let's see"
