import unittest
from pathlib import Path
from src.classes.BlockChain import BlockChain
from src.classes.Node import Node
from src.constants import REPO_PATH
from src.utils.cryptography import sha256


class TestNode(unittest.TestCase):

    def setUp(self):
        self.config_dir_path = Path(REPO_PATH) / \
            "tests/test_data/node_test_config/node0"
        self.node = Node(config_dir_path=self.config_dir_path)

    def test_node_initialization(self):
        self.assertIsNotNone(self.node)
        # Assuming the default port is 5000
        self.assertEqual(self.node.port, "5000")
        self.assertIsInstance(self.node.get_blockchain(), BlockChain)

    def test_generate_block(self):
        test_data = "Test block data"
        prev_block = self.node.get_blockchain().get_last_block()
        new_block = self.node.generate_block(test_data)
        expected_hash = sha256(
            prev_block.block_hash + test_data + str(new_block.height) + str(new_block.nonce))
        self.assertEqual(new_block.block_hash, expected_hash)
        self.assertEqual(new_block.data, test_data)

    # Add more test cases here...


if __name__ == '__main__':
    unittest.main()
