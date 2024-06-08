import os
import unittest

from src.helpers.text import Text
from src.managers.manager import Manager
from unittest.mock import patch, MagicMock
from io import StringIO


class TestManager(unittest.TestCase):
    def setUp(self):
        self.manager = Manager()

    def tearDown(self):
        if os.path.exists("/Users/igorsarnowski/PycharmProjects/cipher/tests/test.json"):
            os.remove("/Users/igorsarnowski/PycharmProjects/cipher/tests/test.json")

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

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_memory_buffer_in_manager(self, mock_out):
        text = Text(text="example", rot_type="rot47", status="decrypted")
        self.manager.memory.add_text(text)
        self.manager.display_memory_buffer()
        self.assertIn("Text(text='example', rot_type='rot47', status='decrypted')", mock_out.getvalue())
        self.manager.clear_memory()

    @patch('builtins.input', return_value="/Users/igorsarnowski/PycharmProjects/cipher/tests/test_read_manager.json")
    def test_read_from_file_in_manager(self, mock_input):
        text = Text("str", "rot13", "encrypted")
        test_list = [text]
        self.manager.read_from_file()
        self.assertEqual(self.manager.memory.buffer, test_list)
        self.manager.clear_memory()

    @patch('builtins.input',
           side_effect=["test.json", "/Users/igorsarnowski/PycharmProjects/cipher/tests/test.json"])
    def test_save_to_file_in_manager(self, mock_input):
        text = Text("str", "rot13", "encrypted")
        test_list = [text]
        self.manager.memory.add_text(text)
        self.manager.save_to_file()
        self.manager.clear_memory()
        self.manager.read_from_file()
        self.assertEqual(self.manager.memory.buffer, test_list)
        self.manager.clear_memory()

    @patch("builtins.input", return_value="neohm")
    def test_clear_memory(self, mock_input):
        self.manager.encrypt_rot13()
        self.manager.clear_memory()
        self.assertEqual(len(self.manager.memory.buffer), 0)

    def test_exit_program(self):
        with self.assertRaises(SystemExit) as cm:
            Manager.exit_program()
        self.assertIsNone(cm.exception.code)
