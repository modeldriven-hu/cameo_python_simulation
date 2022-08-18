from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'halfAge': 21,
                       'isZsolt': True})

@app.route('/calculate',methods = ['POST'])
def calculate():
    json = request.get_json()
    result = json['email'] + " is " + str(json["age"]) + " years old."
    return jsonify({"result": result})

app.run()