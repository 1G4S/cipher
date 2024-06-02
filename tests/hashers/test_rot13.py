import unittest
from src.hashers.rot13 import ROT13


class TestRot13(unittest.TestCase):
    def setUp(self):
        self.rot13 = ROT13()

    def test_encrypt_rot13_for_single_word(self):
        before_encrypt1 = "arbuz"
        self.assertEqual(self.rot13.encrypt(text=before_encrypt1), "neohm")

    def test_encrypt_rot13_for_several_words_first_type(self):
        before_encrypt2 = "ptaki lataja kluczem"
        self.assertEqual(
            self.rot13.encrypt(text=before_encrypt2), "cgnxv yngnwn xyhpmrz"
        )

    def test_encrypt_rot13_for_several_words_second_type(self):
        before_encrypt3 = "project errors"
        self.assertEqual(self.rot13.encrypt(text=before_encrypt3), "cebwrpg reebef")

    def test_decrypt_rot13_for_single_word(self):
        before_decrypt1 = "neohm"
        self.assertEqual(self.rot13.decrypt(text=before_decrypt1), "arbuz")

    def test_decrypt_rot13_for_several_words_first_type(self):
        before_decrypt2 = "cgnxv yngnwn xyhpmrz"
        self.assertEqual(
            self.rot13.decrypt(text=before_decrypt2), "ptaki lataja kluczem"
        )

    def test_decrypt_rot13_for_several_words_second_type(self):
        before_decrypt3 = "cebwrpg reebef"
        self.assertEqual(self.rot13.decrypt(text=before_decrypt3), "project errors")
