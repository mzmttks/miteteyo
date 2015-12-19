from flask import Flask, request
from pymongo import MongoClient
import os
import json
import pprint
app = Flask(__name__)

client = MongoClient(os.environ["MONGOLAB_URI"])
db = client.miteteyo
col = db.locations
print col

@app.route('/location', methods=["POST"])
def addLocation():
  col.insert(request.data)

@app.route('/')
def hello_world():
  locs = [d for d in col.find({})]
  return pprint.pformat(locs)

if __name__ == '__main__':
  app.run(debug=True)
