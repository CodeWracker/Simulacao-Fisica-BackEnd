from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cont = 0
pos = [
    {
        'id': 0,
        'center_x': 100,
        'center_y': 100,
        'radius': 20
    },
    {
        'id': 1,
        'center_x': 50,
        'center_y': 150,
        'radius': 20
    }
]

@app.route('/')
def plus():
    global cont

    while True:

        
        cont = cont + 2
        if(cont>900):
            cont = 0
        global pos
        pos = [
            {
                'id': 0,
                'center_x': 100 + cont,
                'center_y': 100,
                'radius': 20
            },
            {
                'id': 1,
                'center_x': 50 + cont,
                'center_y': 150,
                'radius': 20
            }
        ]
        
        
        return jsonify(pos)
