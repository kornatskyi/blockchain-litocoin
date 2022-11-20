import json


class Block:
    """
    The block on block chaine
    """
    def __init__(self, data: str, block_hash: str, nonce: int, height: int) -> None:
        """
        Constructor
        """
        self.data = data
        self.block_hash = block_hash
        self.nonce = nonce
        self.height = height
    
    def get_block_data_string(self):
        """
        Returns string representations of all blocks data
        needed for generating hash
        (execept prev block hash)!TODO:may need rethinking
        """
        return self.data + str(self.height) + str(self.nonce)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
