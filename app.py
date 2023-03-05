import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200


@app.route('/dialogflow', methods=['GET', 'POST'])
def dialogflow():

    data = request.get_json()
    print(json.dumps(data))

    return jsonify(
        {
            'fulfillment_response': {
                'messages': [
                    {
                        'text': {
                            'text': ['This is a sample rewponse from webhopok.']
                        }
                    }
                ]
            }
        }
    )


if __name__ == '__main__':
    app.run(debug=True)
