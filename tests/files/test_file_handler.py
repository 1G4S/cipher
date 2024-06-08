import unittest
import os
from src.files.file_handler import FileHandler
from src.hashers.text import Text


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_output.json"
        self.test_data = [Text("str", "rot13", "encrypted"), Text('str', 'rot47', 'encrypted'),
                          Text('st1234', 'rot13', 'encrypted')]
        self.test_data_to_read_from_file = [Text("str", "rot13", "encrypted"), Text('str12', 'rot13', 'decrypted'),
                                            Text('str32', 'rot47', 'encrypted')]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_text_to_file_creates_file_in_file_handler(self):
        FileHandler.save_text_to_file(data=self.test_data, filename=self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_save_text_to_file_content_in_file_handler(self):
        FileHandler.save_text_to_file(data=self.test_data, filename=self.test_file)
        data_read = FileHandler.read_from_file(self.test_file)
        self.assertEqual(data_read, self.test_data)

    def test_read_from_file_in_file_handler(self):
        data_read = FileHandler.read_from_file(path="test_read.json")
        self.assertEqual(self.test_data_to_read_from_file, data_read)

    def test_is_filename_valid_for_right_value(self):
        filename = "python.json"
        self.assertEqual(FileHandler.is_filename_valid(filename), True)

    def test_is_filename_valid_for_wrong_value(self):
        filename = "python.jsn"
        self.assertEqual(FileHandler.is_filename_valid(filename), False)
