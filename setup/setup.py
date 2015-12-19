import subprocess
import pymongo

url = subprocess.check_output("heroku config | grep MONGO | cut -d' ' -f 2", shell=True).rstrip()
db = url.split("/")[-1]
client = pymongo.MongoClient(url)
print client[db].locations.create_index("userid")
