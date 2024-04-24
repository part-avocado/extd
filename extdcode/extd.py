import sys
from errorcodes import err
from okcodes import ok

def errorExit(code, message = None):
  err(code, message)
  sys.exit()
def raiseError(code, message = None):
  err(code, message)
  return code
def okCode(code, message = None, respond = None):
  ok(code, message)
  if respond == True:
    return code
  elif respond == False or respond == None:
    pass
