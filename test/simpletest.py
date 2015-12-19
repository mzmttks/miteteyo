import requests

# host = "https://miteteyo.herokuapp.com"
host = "http://localhost:5000"

print "POSTING"
ret = requests.post(host + "/location", json={'Mytest': 3},
                    headers={'Content-Type': 'application/json'})
print ret.text

print "GETTING"
ret = requests.get(host + "/userid")
print ret.text

print "GETTING"
ret = requests.get(host + "/userid/foobar")
print ret.text

print "GETTING"
ret = requests.get(host)
print ret.text
