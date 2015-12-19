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
  try:
    print "REQUEST.JSON", "---", request.json, "---"
    col.insert_one(request.json)
  except Exception as e:
    import traceback
    print traceback.format_exc()
  

@app.route('/')
def hello_world():
  locs = [d for d in col.find({})]
  print pprint.pformat(locs)
  return pprint.pformat(locs)

if __name__ == '__main__':
  app.run(debug=True)
