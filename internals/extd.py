import sys
from errocodes import err

def errorExit(code, message = None):
  err(code, message)
  sys.exit()
def raiseError(code, message = None):
  err(code, message)
  return code

