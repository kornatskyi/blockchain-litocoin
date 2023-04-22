import hashlib

# *____Utils____*
# simplify calling sha256 function from hashlib, returns hexidesimal value
def sha256(message):
  return hashlib.sha256(message.encode("utf-8")).hexdigest()
