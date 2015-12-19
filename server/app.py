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
  print "REQUEST.JSON"
  print "---", request.json, "---"
  print "---", col.insert_one(request.data)
  

@app.route('/')
def hello_world():
  locs = [d for d in col.find({})]
  print pprint.pformat(locs)
  return pprint.pformat(locs)

if __name__ == '__main__':
  app.run(debug=True)
