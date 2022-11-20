import json
from pathlib import Path
from src.classes.Block import Block
from src.utils.cryptography import sha256



class BlockChain:
    """
    Class reperesenting Block chain
    """

    def __init__(self, blockchain_file_path: Path) -> None:
        self.blockchain_file_path = blockchain_file_path
        self.root_block = None
        self.blocks: list[Block] = []

    def load_blockchain_from_file(self) -> None:
        """
        Loads blockchain from file to the memory
        """
        blocks_json = None
        self.blocks = []
        with open(self.blockchain_file_path, 'rb') as file:
            blocks_json = json.load(file)["blocks"]
        for block_json in blocks_json:
            loaded_block = Block(block_json["data"],
                                 block_json["hash"],
                                 int(block_json["nonce"]),
                                 int(block_json["height"]))
            self.blocks.append(loaded_block)

    def validate_blockchain(self):
        """
        Validates all blocks in blockchain
        """
        # sort blocks firs by its height
        self.blocks.sort(key=lambda block: block.height)
        for i in range(1, len(self.blocks)):
            prev_block = self.blocks[i - 1]
            validate_block_hash(self.blocks[i], prev_block.block_hash)


def validate_block_hash(block: Block, prev_block_hash: str):
    assert block.block_hash == sha256(prev_block_hash + block.get_block_data_string())

