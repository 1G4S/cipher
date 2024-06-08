import unittest

from src.helpers.text import Text
from src.managers.manager import Manager
from unittest.mock import patch, MagicMock


class TestManager(unittest.TestCase):
    def setUp(self):
        self.manager = Manager()

    @patch("builtins.input", return_value="arbuz")
    def test_encrypt_rot13_in_manager(self, mock_input):
        text = Text("neohm", "rot13", "encrypted")
        self.manager.encrypt_rot13()
        self.assertEqual(self.manager.memory.buffer[0], text)
        self.manager.clear_memory()
