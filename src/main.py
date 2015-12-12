import threading
import time

def nemaParse(line):
  parts = line.rstrip("\r\n").split(",")
  if "$GPRMC" in line:
    keys = ["code", "time", "status", "latitude", "NorS", 
            "longtitude", "EorW",
            "speed", "direction", "date", 
            "magnetic", "magneticEorW",
            "mode", "checksum"]
    return dict(zip(keys, parts))
  if "$GPGGA" in line:
    keys = ["code", "time", "latitude", "NorS", 
            "longtitude", "EorW",
            "quality", "satellites", "quality_degration", "height", 
            "magnetic", "magneticEorW",
            "mode", "checksum"]
    return dict(zip(keys, parts))
  if "$GPGSA" in line:
    return parts
  if "$GPGSV" in line:
    return parts
  if "$GPVTG" in line:
    return parts

  return None


def conv(obj):
  return {
    "status": obj["status"],
    "date": obj["date"] + obj["time"],
    "latitude": obj["latitude"] + obj["NorS"],
    "longtitude": obj["longtitude"] + obj["EorW"],
    "speed": float(obj["speed"]) * 1852 / 3600
  }

if __name__ == "__main__":
  dev = "/dev/ttyAMA0"
  handle = open(dev)
  try:
    while 1:
      line = handle.readline()
      if "$GPRMC" in line:
        print conv(nemaParse(line))
  finally:
    if handle is not None:
      handle.close()
