import json
from pathlib import Path

from src.classes import BlockChain




class Node:
    """
    Represend node on a blockchain
    """
    def __init__(self, config_file_path: Path, blockchain_file_path: Path):
        jsondata = config_file_path.read_text()
        self.name = json.loads(jsondata)["name"]
        self.port = json.loads(jsondata)["port"]
        self.blockchain = BlockChain(blockchain_file_path)

    def set_name(self, new_name: str) -> None:
        """
        Name setter
        """
        self.name = new_name
        