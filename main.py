import json

from flask import Flask
from flask import request

from backedn_call import get_open_ai_response

app = Flask(__name__)

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
    app.run()