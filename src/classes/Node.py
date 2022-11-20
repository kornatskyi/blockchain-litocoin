import json
from pathlib import Path
from src.classes.Block import Block
from src.classes.BlockChain import BlockChain
from src.constants import REPO_PATH
from src.utils.cryptography import sha256


class Node:
    """
    Represend node on a blockchain
    """

    def __init__(self, config_dir_path: Path):
        self.config_file_path = Path(config_dir_path) / "config.json"
        assert self.config_file_path.exists(), f"No config file in a directory {config_dir_path}"
        jsondata = self.config_file_path.read_text()
        self.name = json.loads(jsondata)["name"]
        self.port = json.loads(jsondata)["port"]
        
        self.blockchain_file_path = Path(
            REPO_PATH) / config_dir_path.__str__() / "blockchain.json"
        assert self.blockchain_file_path.exists(), f"No blockchain file in {self.blockchain_file_path.__str__()}"
        self.blockchain = BlockChain(self.blockchain_file_path)

    def set_name(self, new_name: str) -> None:
        """
        Name setter
        """
        self.name = new_name

    def get_blockchain(self):
        """
        Returns blockchain to which this node refers to
        """
        return self.blockchain


def generate_block(prev_block: Block, new_block_data: str, number_of_leading_zeros: int) -> Block:
    """
    Generate new block with special hash, which has leading zeros
    BLOCK DATA ORDER for hashing:
    (everething is string type)
    0. Previous block hash
    1. New block data(message)
    2. New height in string format
    3. New nonce
    """
    block_height = prev_block.height + 1
    block_data = prev_block.block_hash + new_block_data + str(block_height)
    new_hash = ''
    nonce = 0
    while new_hash[:number_of_leading_zeros] != ("0" * number_of_leading_zeros):
        nonce = nonce + 1
        new_hash = sha256(block_data + str(nonce))
    return Block(new_block_data, new_hash, nonce, block_height)
