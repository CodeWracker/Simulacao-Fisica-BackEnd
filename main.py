from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
pos = [
    {
        'id': 0,
        'center[2]': [100, 100],
        'radius': 2
    },
    {
        'id':1,
        'center[2]': [50, 150],
        'radius': 2
    }
]

@app.route('/')
def home():
    return jsonify(pos)