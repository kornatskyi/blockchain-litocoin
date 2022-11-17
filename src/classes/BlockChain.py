import json
from src.classes.Blcok import Block


class BlockChain:
  def __init__(self) -> None: 
    jsondata = open("./blockchain.json", 'r')
    root_block_data =json.load(jsondata)["root"]
    self.root = Block(root_block_data["data"], root_block_data["hash"])
    pass