def parse(line):
  parts = line.rstrip("\r\n").split(",")
  if "$GPRMC" in line:
    return parts
  if "$GPGGA" in line:
    return parts
  if "$GPGSA" in line:
    return parts
  if "$GPGSV" in line:
    return parts
  if "$GPVTG" in line:
    return parts

  return None

