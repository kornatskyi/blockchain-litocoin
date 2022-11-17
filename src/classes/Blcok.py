class Block:
  def __init__(self, data:str, prev_hash:str) -> None:
    self.data = data
    self.prev_hash = prev_hash
    pass