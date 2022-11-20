
from src.classes import Block
from src.utils.cryptography import sha256

p_b= Block("some block", "0", 0)

def generate_block(prev_block: Block, new_block_data: str, number_of_leading_zeros: int) -> Block:
    """
    Generate new block with special hash, which has leading zeros
    """
    block_data = new_block_data + prev_block.data + prev_block.block_hash
    new_hash = ''
    nonce = 0
    while new_hash[:number_of_leading_zeros] != ("0" * number_of_leading_zeros):
        nonce = nonce + 1
        new_hash = sha256(block_data + str(nonce))
    return Block(new_block_data, new_hash, nonce)