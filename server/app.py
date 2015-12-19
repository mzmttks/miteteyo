from flask import jsonify, Flask, request
from pymongo import MongoClient
import os
import json
import pprint
import traceback
app = Flask(__name__)

client = MongoClient(os.environ["MONGOLAB_URI"])
db = client["heroku_gw4w78g9"]
col = db["locations"]
print col

@app.route('/location', methods=["POST"])
def addLocation():
  try:
    data = request.json
  except Exception as e:
    ret = jsonify({"msg": "JSON parsing failed"})
    ret.status_code = 400
    return ret

  keys = ["latitude", "longitude", "userid", "utcTime"]
  for key in keys:
    if key not in data.keys():
      ret = jsonify({"msg": "Mandatory key %s is not found" % key})
      ret.status_code = 400
      return ret

  col.insert_one(request.json)
  return "ok" 

@app.route('/userid')
def getUserid():
  userids = col.distinct("userid")
  return jsonify({"userids": userids})

@app.route('/userid/<userid>')
def getLocations(userid):
  locs = []
  for d in col.find({"userid": userid}):
    del d["_id"]
    locs.append(d)
  return jsonify({"locations": locs})

@app.route('/')
def hello_world():
  locs = [d for d in col.find({})]
  return "<pre>" + pprint.pformat(locs) + "</pre>"

if __name__ == '__main__':
  app.run(debug=True)
