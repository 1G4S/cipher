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

    @patch("builtins.input", return_value="neohm")
    def test_decrypt_rot13_in_manager(self, mock_input):
        text = Text("arbuz", "rot13", "decrypted")
        self.manager.decrypt_rot13()
        self.assertEqual(self.manager.memory.buffer[0], text)
        self.manager.clear_memory()

    @patch("builtins.input", return_value="project errors")
    def test_encrypt_rot47_in_manager(self, mock_input):
        text = Text("AC@;64E 6CC@CD", "rot47", "encrypted")
        self.manager.encrypt_rot47()
        self.assertEqual(self.manager.memory.buffer[0], text)
        self.manager.clear_memory()

    @patch("builtins.input", return_value="AC@;64E 6CC@CD")
    def test_decrypt_rot47_in_manager(self, mock_input):
        text = Text("project errors", "rot47", "decrypted")
        self.manager.decrypt_rot47()
        self.assertEqual(self.manager.memory.buffer[0], text)
        self.manager.clear_memory()
