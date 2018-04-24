from flask import Flask, request, abort, jsonify, json, session
from flask.ext.session import Session


import sys
sys.path.insert(0, '../engine')

import Guide as guide
import guard as x
import dto

sess = Session()

app = Flask(__name__)

guard = x.Guard()
guidex = guide.Guide()

@app.route('/', methods=['POST'])
def authenticate():
    print(request.json)
    if not request.json:
        abort(400)
    else:
        obj = request.json
        res = guard.Authenticate(obj["username"], obj["password"])
        session["loggedin"] = True
        return jsonify({ "ok" : str(res.success), "message": res.message}), 201

@app.route('/getWorkTypes', methods=['GET'])
def getWorkTypes():
    print(session["loggedin"])
    types = guidex.getWorkTypes()
    return jsonify({ "data" : types }), 201

@app.route('/getWorkSubTypes', methods=['POST'])
def getWorkSubTypes():
    obj = request.json
    types = guidex.getWorkSubTypes(obj["parentId"])
    return jsonify({ "data" : types }), 201

@app.route('/getMoodTypes', methods=['GET'])
def getMoodTypes():
    types = guidex.getMoodTypes()
    return jsonify({ "data" : types }), 201

@app.route('/getWelcomeMessage', methods=['GET'])
def getWelcomeMessage():
    message = guidex.getWelcomeMessage()
    return jsonify({ "data" : message }), 201

@app.route('/reportMood', methods=['POST'])
def reportMood():
    print(request.json)
    if not request.json:
        abort(400)
    else:
        obj = request.json

        report = dto.moodReport(0, request.json["mood"], 0, request.json["reason"])
        res = guidex.reportMood(report)
        return jsonify({ "ok" : str(res)}), 201

if __name__ == '__main__':

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.run(debug=True)
