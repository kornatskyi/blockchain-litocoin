import unittest
from pathlib import Path
from src.classes.BlockChain import BlockChain
from src.classes.Node import Node, generate_block
from src.constants import REPO_PATH
from src.rules import NUMBER_OF_LEADING_ZEROS

class TestBlockChain(unittest.TestCase):

    def setUp(self):
        self.config_dir_path = Path(REPO_PATH) / \
            "tests/test_data/node_test_config/node0"
        self.node = Node(config_dir_path=self.config_dir_path)

    def test_block_chain_initialization(self):
        self.assertIsNotNone(self.node.get_blockchain())
        self.assertIsInstance(self.node.get_blockchain(), BlockChain)

    def test_block_chain_length(self):
        self.assertEqual(len(self.node.get_blockchain().get_blocks()), 11)

    def test_block_chain_last_block(self):
        self.assertEqual(self.node.get_blockchain().get_last_block(),
                         self.node.get_blockchain().get_blocks()[-1])

    def test_block_chain_add_block(self):
        test_data = "Test block data"
        prev_block = self.node.get_blockchain().get_last_block()
        new_block = generate_block(new_block_data=test_data, prev_block=prev_block,
                                   number_of_leading_zeros=NUMBER_OF_LEADING_ZEROS)
        self.node.get_blockchain().add_a_block(new_block)


if __name__ == '__main__':
    unittest.main()
