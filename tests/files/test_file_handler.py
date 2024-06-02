import json
import unittest
import os
from src.files.file_handler import FileHandler
from src.hashers.text import Text


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_output.json"
        self.test_data = Text("str", "rot13", "encrypted")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_text_to_file_creates_file_in_file_handler(self):
        FileHandler.save_text_to_file(data=self.test_data, filename=self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_save_text_to_file_content_in_file_handler(self):
        FileHandler.save_text_to_file(data=self.test_data, filename=self.test_file)

        with open(self.test_file) as file:
            data = json.load(file)
        data_read = Text(data["text"], data["rot_type"], data["status"])
        self.assertEqual(data_read, self.test_data)

    def test_read_from_file_in_file_handler(self):
        data = Text("str", "rot13", "encrypted")
        data_read = FileHandler.read_from_file(path="test_read.json")
        self.assertEqual(data, data_read)

    def test_validation_in_file_handler_for_right_value(self):
        data_to_validate = Text("str", "rot13", "encrypted")
        self.assertEqual(FileHandler.validation(data=data_to_validate), False)

    def test_validation_in_file_handler_for_wrong_value(self):
        data_to_validate = Text("str", "rot13", "encrypteerrd")
        self.assertEqual(FileHandler.validation(data=data_to_validate), True)
