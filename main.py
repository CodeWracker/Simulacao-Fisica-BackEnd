from flask import Flask, jsonify

app = Flask(__name__)

pos = [
    {
        'id': 0,
        'center[2]': [100, 100],
        'radius': 2
    },
    {
        'id':1,
        'center[2]': [150, 150],
        'radius': 2
    }
]

@app.route('/')
def home():
    return jsonify(pos)