import json
from pathlib import Path
from src.classes.Block import Block
from src.utils.cryptography import sha256

class BlockChain:
    """
    Class representing Block chain
    """

    def __init__(self, blockchain_file_path: Path) -> None:
        self._blockchain_file_path = blockchain_file_path
        self._root_block = None
        self._blocks: list[Block] = []
    
    def get_blocks(self) -> list[Block]:
        """
        Returns blockchain blocks
        """
        return self._blocks 

    def load_blockchain_from_the_file(self) -> None:
        """
        Loads blockchain from file to the memory
        """
        blocks_json = None
        self._blocks = []
        with open(self._blockchain_file_path, mode='r', encoding="utf-8") as file:
            blocks_json = json.load(file)
        for block_json in blocks_json:
            loaded_block = Block(block_json["data"],
                                 block_json["block_hash"],
                                 int(block_json["nonce"]),
                                 int(block_json["height"]))
            self._blocks.append(loaded_block)

    def load_blockchain_from_the_json(self, blocks_json:str) -> None:
        """
        Loads blockchain from the json
        !!! TODO need a better way to handle blockchain in json format
        """
        self._blocks = []
        blocks_json = json.loads(blocks_json)
        for block_json in blocks_json:
            block_json = json.loads(block_json)
            loaded_block = Block(block_json["data"],
                                    block_json["block_hash"],
                                    block_json["nonce"],
                                    block_json["height"])
            self._blocks.append(loaded_block)


    def write_blockchain_to_the_file(self) -> None:
        """
        Writes all blockchain from the memory to the file in json format
        """
        blocks_dict = [block.__dict__ for block in self._blocks]

        with open(self._blockchain_file_path, mode='w', encoding="utf-8") as file:
            file.write(json.dumps(blocks_dict, sort_keys=True, indent=4))

    def validate_blockchain(self):
        """
        Validates all blocks in blockchain
        """
        # sort blocks firs by its height
        self._blocks.sort(key=lambda block: block.height)
        for i in range(1, len(self._blocks)):
            prev_block = self._blocks[i - 1]
            if not is_block_hash_valid(self._blocks[i], prev_block.block_hash):
                raise Exception("Fail to validation. Blockchain ins't valid!")
    
    def get_last_block(self) -> Block:
        """
        Return the last(best) block from the blockchain
        """
        return self._blocks[-1]

    def add_a_block(self, block: Block) -> None:
        """
        Adds block to the blockchain
        """
        self._blocks.append(block)


def is_block_hash_valid(block: Block, prev_block_hash: str) -> bool:
    """
    Validates if block hash is valid
    """
    return block.block_hash == sha256(prev_block_hash + block.get_block_data_string())

