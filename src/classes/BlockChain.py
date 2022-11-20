import json

from click import Path
from src.classes.Block import Block


class BlockChain:
    """
    Class reperesenting Block chain
    """

    def __init__(self, blockchain_file_path: Path) -> None:
        with open(blockchain_file_path, 'rb') as file:
            root_block_data = json.load(file)["root"]
            self.root = Block(root_block_data["data"], root_block_data["hash"])
