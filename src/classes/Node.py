import json
from pathlib import Path
from src.classes.Singleton import Singleton
from src.classes.Block import Block
from src.classes.BlockChain import BlockChain
from src.constants import REPO_PATH
from src.rules import NUMBER_OF_LEADING_ZEROS
from src.utils.cryptography import sha256


class Node(metaclass=Singleton):
    """
    Represent node on a blockchain
    """
    def __init__(self, config_dir_path:Path=None):
        self._config_file_path = Path(config_dir_path) / "config.json"
        assert self._config_file_path.exists(
        ), f"No config file in a directory {config_dir_path}"
        jsondata = self._config_file_path.read_text()
        self._name = json.loads(jsondata)["name"]
        self._port = json.loads(jsondata)["port"]

        self._blockchain_file_path = Path(
            REPO_PATH) / config_dir_path.__str__() / "blockchain.json"

        assert self._blockchain_file_path.exists(
        ), f"No blockchain file in {self._blockchain_file_path.__str__()}"

        self._blockchain = BlockChain(self._blockchain_file_path)

    def set_name(self, new_name: str) -> None:
        """
        Name setter
        """
        self._name = new_name

    def get_name(self) -> str:
        """
        Get nodes name
        """
        return self._name
    
    def get_port(self) -> int:
        """
        Get a port for this node's server 
        """
        return self._port

    def get_blockchain(self):
        """
        Returns blockchain to which this node refers to
        """
        return self._blockchain

    def generate_block(self, block_data: str) -> Block:
        """
        Node generates new block
        """
        new_block = generate_block(
            self._blockchain.get_last_block(), block_data, NUMBER_OF_LEADING_ZEROS)
        return new_block


def generate_block(prev_block: Block, new_block_data: str, number_of_leading_zeros: int) -> Block:
    """
    Generate new block with special hash, which has leading zeros
    BLOCK DATA ORDER for hashing:
    (everything is string type)
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
