#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

# Modified by sngc1 Dec 2015
import os
from gps import *
from time import *
import time
import threading
import httplib

SERVER_ADDRESS = 'https://miteteyo.herokuapp.com'
SERVER_RESOURCE = '/location'
HEADERS = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
USERID = 'test1'

gpsd = None #seting the global variable
os.system('clear') #clear the terminal (optional)
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

def postGpsData(userid, latitude, longitude, utcTime):
  params = urllib.urlencode({'userid': userid, 'latitude': latitude, 'longitude': longitude, 'utcTime': utcTime})
  headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

  conn = httplib.HTTPSConnection(SERVER_ADDRESS)
  conn.request("POST", SERVER_RESOURCE, params, HEADERS)
  res = conn.getresponse()
  print res.status, res.reason
  #data = res.read()
  conn.close()

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
 
      os.system('clear')

      latitude = gpsd.fix.latitude
      longitude = gpsd.fix.longitude
      utcTime = gpsd.utc,' + ', gpsd.fix.time
      
      print
      print ' GPS reading'
      print '----------------------------------------'
      print 'latitude    ' , gpsd.fix.latitude
      print 'longitude   ' , gpsd.fix.longitude
      print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
      print 'altitude (m)' , gpsd.fix.altitude
      print 'eps         ' , gpsd.fix.eps
      print 'epx         ' , gpsd.fix.epx
      print 'epv         ' , gpsd.fix.epv
      print 'ept         ' , gpsd.fix.ept
      print 'speed (m/s) ' , gpsd.fix.speed
      print 'climb       ' , gpsd.fix.climb
      print 'track       ' , gpsd.fix.track
      print 'mode        ' , gpsd.fix.mode
      print
      print 'sats        ' , gpsd.satellites
 
      time.sleep(5) #set to whatever

      postGpsData(USERID, latitude, longitude, utcTime)
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
