class Block:
    """
    The block on block chaine
    """
    def __init__(self, data: str, block_hash: str, nonce: int) -> None:
        """
        Constructor
        """
        self.data = data
        self.block_hash = block_hash
        self.nonce = nonce
