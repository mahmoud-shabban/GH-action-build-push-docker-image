from crypt import methods
import logging
import mimetypes
from urllib import response
from flask import Flask
import json
app = Flask(__name__)



@app.route('/status')
def status():
  response = app.response_class(
          response=json.dumps({"result":"OK - healthy"}),
          status=200,
          mimetype='application/json'
  )
  return response

@app.route('/metrics')
def metrics():
  response = app.response_class(
          response=json.dumps({"status":"success", 'code':0,'data':{'UserCount':140, 'UserCountActive':23}}),
          status=200,
          mimetype='application/json'
  )
  return response



@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
  logging.basicConfig(filemode= 'app.log', level= logging.DEBUG)
  app.run(host='0.0.0.0')
