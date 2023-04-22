from pathlib import Path
import unittest
from src.classes import Node
from src.constants import REPO_PATH
from src.flaskr.flask_server import create_app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.config_dir_path = Path(REPO_PATH) / \
            "tests/test_data/node_test_config/node0"
        self.node = Node(config_dir_path=self.config_dir_path)
        self.app = create_app()
        self.client = self.app.test_client()

    def test_generate_block(self):
        response = self.client.get("/info/blockchain")
        self.assertEqual(response.status_code, 200)
        # !TODO: Add more assertions to check the response content
