import json
from src.classes.Block import Block


class BlockChain:
    """
    Class reperesenting Block chain
    """

    def __init__(self) -> None:
        with open("./blockchain.json", 'rb') as file:
            root_block_data = json.load(file)["root"]
            self.root = Block(root_block_data["data"], root_block_data["hash"])
