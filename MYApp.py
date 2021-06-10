from flask import Flask, app, json, jsonify, request
from werkzeug.wrappers import response
##Multiple route example routes= enpoints
app1 = Flask(__name__)


STATUS={"user": "admin","result": "OK - healthy"}
DATA={"user": "admin","data": {"UserCount": 140, "UserCountActive": 23}}

@app1.route("/") # main route 
def hello():
    return "hello world"

@app1.route('/status')
def status():
    return jsonify(STATUS)

@app1.route('/status1')
def status1():
    return jsonify(STATUS)
@app1.route('/metrics')
def metrics():
    response=app1.response_class(response=json.dumps(DATA),
                                status=200,
                                mimetype='application/json')
    return response

if __name__ == "__main__":
    app1.run(host='0.0.0.0')
