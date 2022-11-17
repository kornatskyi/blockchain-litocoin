import json
from pathlib import Path


class Node:
  def __init__(self, env_file_path: Path):
    jsondata = env_file_path.read_text()
    self.name =json.loads(jsondata)["name"]
    self.port = json.loads(jsondata)["port"]
    pass

  def set_name(self, new_name:str) -> None:
    self.name = new_name
  pass
