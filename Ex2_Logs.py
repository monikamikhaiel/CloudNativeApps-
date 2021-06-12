from flask import Flask, app, json, jsonify, request
import logging
import datetime 
##the timestamp 
# log format -> "{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached"
current_time = datetime.datetime.now()
TimeStamp=current_time.strftime("%I:%M %p at %d-%B-%Y ")
print(TimeStamp)
## creating logs 
logging.basicConfig(filename='app.log',encoding='utf-8', level=logging.DEBUG
                    ,format='%(levelname)s: %(asctime)s ,%(message)s endpoint was reached')
##Multiple route example routes= enpoints
app1 = Flask(__name__)


STATUS={"user": "admin","result": "OK - healthy"}
DATA={"user": "admin","data": {"UserCount": 140, "UserCountActive": 23}}

@app1.route("/") # main route 
def hello():
    message= TimeStamp +","+ "main route "+ "endpoint was reached"
    logging.debug("main route ")
    return "hello world"

@app1.route('/status')
def status():
    message= TimeStamp +","+ "status route "+ "endpoint was reached"
    logging.debug("status route ")
    return jsonify(STATUS)

@app1.route('/status1')
def status1():
    return jsonify(STATUS)
@app1.route('/metrics')
def metrics():
    response=app1.response_class(response=json.dumps(DATA),
                                status=200,
                                mimetype='application/json')
    message= TimeStamp +","+ "metrics route  "+ "endpoint was reached"
    logging.debug("metrics route  ")
    return response

if __name__ == "__main__":
    app1.run(host='0.0.0.0')
    app1.run(debug=True)
    
