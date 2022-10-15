import json
import os

from flask import Flask
from flask import request, send_from_directory

from backedn_call import get_open_ai_response

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/favicon.png'
    )

@app.route('/', methods=['GET'])
def home():
    return json.dumps(
        {
            'status': 1,
            'message': 'Success.'
        }
    )

@app.route('/api/explain_code/', methods=['POST'])
def explain_code():
    data = request.data
    data = json.loads(data)
    code = data['code']
    response = get_open_ai_response(code=code)
    return json.dumps(response)

if __name__ == '__main__':
    app.run(
        port=os.getenv('PORT')
    )