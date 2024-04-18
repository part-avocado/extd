import sys
from exit_err import exit_err
from err import err

def errorExit(code, message = None):
  exit_err(code, message)
  sys.exit()
def raiseError(code, message = None):
  err(code, message)
  return
