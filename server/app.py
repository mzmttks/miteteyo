from flask import Flask, request
from pymongo import MongoClient
import os
import json
import pprint
app = Flask(__name__)

client = MongoClient(os.environ["MONGOLAB_URI"])
db = client["heroku_gw4w78g9"]
col = db["locations"]
print col

@app.route('/location', methods=["POST"])
def addLocation():
  print request.data
  try:
    col.insert_one(request.json)
  except Exception as e:
    import traceback
    print traceback.format_exc()
  return "ok" 

@app.route('/')
def hello_world():
  locs = [d for d in col.find({})]
  print pprint.pformat(locs)
  return "<pre>" + pprint.pformat(locs) + "</pre>"

if __name__ == '__main__':
  app.run(debug=True)
