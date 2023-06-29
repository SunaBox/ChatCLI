import unittest
from unittest import TestCase
from fastapi.testclient import TestClient

from src.models import CLIInput
from src.main import app


class TestServer(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_chatgpt_server(self) -> None:
        # データの準備
        chat_log = [{"role": "user", "content": "Hello"}]
        cli_input = {"character": "test", "chat_log": chat_log, "command": "test"}
        cli_input = CLIInput(**cli_input)
        # リクエスト
        response = self.client.post("/", content=cli_input.json())
        # レスポンスの確認
        self.assertEqual(response.status_code, 200)
        response_dict = response.json()
        self.assertIsInstance(response_dict, dict)
        self.assertIn("response", response_dict)
        self.assertIn("command", response_dict)

if __name__ == "__main__":
    unittest.main()
