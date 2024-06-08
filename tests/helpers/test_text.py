import unittest

from src.helpers.text import Text


class TestText(unittest.TestCase):
    def test_is_text_valid_for_right_value(self):
        text = Text("str", "rot13", "encrypted")
        self.assertEqual(text.is_text_valid(), True)

    def test_is_text_valid_for_wrong_value(self):
        text = Text("str", "rot13", "esdancrypted")
        self.assertEqual(text.is_text_valid(), False)

    def test_is_text_from_dict_valid_for_right_value(self):
        text = {"text": "str", "rot_type": "rot13", "status": "encrypted"}
        self.assertEqual(Text.is_text_from_dict_valid(text), True)

    def test_is_text_from_dict_valid_for_wrong_value(self):
        text = {"text": "str", "rot_type": "rot45", "status": "encrypted"}
        self.assertEqual(Text.is_text_from_dict_valid(text), False)

    def test_from_dict_function(self):
        text = Text("str", "rot13", "encrypted")
        text_dict = {"text": "str", "rot_type": "rot13", "status": "encrypted"}
        self.assertEqual(Text.from_dict(text_dict), text)
