from flask import Flask, jsonify
from flask_cors import CORS
import json
quantBalls = 4
app = Flask(__name__)
CORS(app)

with open('db.json') as json_file:
    infos = json.load(json_file)
print(infos)


cont = 0

class Canvas(object):
    def __init__(self):
        self.width = 1000
        self.heigh = 800
canvas = Canvas()
teste= json.dumps(canvas.__dict__)
print(teste)
def obj_dict(obj):
    return obj.__dict__

class Ball(object):
    def __init__(self, x,y,num):
        self.radius = 5
        self.id = num
        self.centerX = x
        self.centerY = y
    def move(self):
        self.centerX = self.centerX + 10
bolas = []
for i in range(quantBalls):
    bolas.append(Ball(50,10*i,i))
for i in range(quantBalls):
    infos["ball"].append(json.dumps(bolas[i].__dict__))
    teste = json.dumps(bolas, default=obj_dict)

@app.route('/')
def plus():
    
    for i in range(quantBalls):
        bolas[i].move()
    print(teste)
    return jsonify(infos)
    
    
    
    


