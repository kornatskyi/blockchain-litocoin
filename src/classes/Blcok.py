class Block:
    """
    The block on block chaine
    """
    def __init__(self, data: str, prev_hash: str) -> None:
        """
        Constructor
        """
        self.data = data
        self.prev_hash = prev_hash
