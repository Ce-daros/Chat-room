from email import message
from warnings import catch_warnings
from flask import Flask, request, jsonify

app = Flask(__name__)
messages=[["",""]]


@app.route('/send', methods=['POST'])
def send_message():
    print("request got.")
    n=request.form.get('name')
    c=request.form.get('content')
    print(n + " said: " + c)
    messages.append([n,c])
    print(messages)
    return 'Success'

@app.route('/get_lastest')
def get_message():
    print("request got.")
    return jsonify(messages[-1])


if __name__ == '__main__':
    app.run(port=5000, debug=True)