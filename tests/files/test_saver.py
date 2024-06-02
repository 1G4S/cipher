import unittest
import os
from src.files.saver import Saver


class TestSaveTextToFile(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_output.txt"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_text_to_file_creates_file(self):
        Saver.save_text_to_file("Hello!", self.test_file)
        self.assertTrue(os.path.exists(self.test_file))

    def test_save_text_to_file_content(self):
        test_text = "Hello!"
        Saver.save_text_to_file(test_text, self.test_file)

        with open(self.test_file, "r") as file:
            content = file.read()

        self.assertEqual(content, test_text)
