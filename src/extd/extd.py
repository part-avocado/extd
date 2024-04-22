import sys
from errorcodes import err

def errorExit(code, message = None):
  err(code, message)
  sys.exit()
def raiseError(code, message = None):
  err(code, message)
  return code

