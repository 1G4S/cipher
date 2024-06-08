import unittest
from src.helpers.text import Text
from src.helpers.memory_buffer import MemoryBuffer


class TestMemoryBuffer(unittest.TestCase):
    def test_add_text(self):
        buffer = MemoryBuffer()
        text1 = Text("12345", "rot13", "encrypted")
        text2 = Text("31254215", "rot47", "decrypted")

        buffer.add_text(text1)
        buffer.add_text(text2)

        self.assertEqual(len(buffer.buffer), 2)
        self.assertIn(text1, buffer.buffer)
        self.assertIn(text2, buffer.buffer)

    def test_add_list_of_text(self):
        buffer = MemoryBuffer()
        text1 = Text("12345", "rot13", "encrypted")
        text2 = Text("31254215", "rot47", "decrypted")
        list1 = [text1, text2]
        buffer.add_list_of_texts(list1)
        self.assertEqual(len(buffer.buffer), 2)

    def test_remove_text(self):
        buffer = MemoryBuffer()
        text1 = Text("12345", "rot13", "encrypted")
        text2 = Text("31254215", "rot47", "decrypted")
        buffer.add_text(text1)
        buffer.add_text(text2)

        buffer.remove_text("12345")

        self.assertEqual(len(buffer.buffer), 1)
        self.assertNotIn(text1, buffer.buffer)
        self.assertIn(text2, buffer.buffer)

    def test_validation_in_memory_buffer_for_right_value(self):
        data_to_validate = Text("str", "rot13", "encrypted")
        self.assertEqual(MemoryBuffer.is_data_valid(data=data_to_validate), True)

    def test_validation_in_memory_buffer_for_wrong_value(self):
        data_to_validate = Text("str", "rot13", "encrypteerrd")
        self.assertEqual(MemoryBuffer.is_data_valid(data=data_to_validate), False)
