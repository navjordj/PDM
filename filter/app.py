from flask import Flask, request

import json

app = Flask(__name__)

@app.route('/data', methods=["POST"])
def recieve_data():
    data = json.loads(request.data)

    print(data)
    return " ", 200

if __name__ == "__main__":
    Flask.run(app, port=5001)