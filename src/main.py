import hashlib
import json
import os
from random import random
from types import SimpleNamespace


 
# Clearing the sonsole
os.system('clear')

# *____Utils____*
# siplify calling sha256 function from hashlib, returns hexidesimal value
def sha256(message):
  return hashlib.sha256(message.encode("utf-8")).hexdigest()



class Block:
  def __init__(self, data:str, prev_hash:str) -> None:
    self.data = data
    self.prev_hash = prev_hash
    pass

class BlockChain:
  def __init__(self) -> None: 
    jsondata = open("./blockchain.json", 'r')
    root_block_data =json.load(jsondata)["root"]
    self.root = Block(root_block_data["data"], root_block_data["hash"])
    pass

class Node:
  
  pass


def main():


  BlockChain()
  pass



if __name__ == "__main__":
    main()
    pass
