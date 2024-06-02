import unittest
from src.hashers.rot47 import ROT47


class TestRot47(unittest.TestCase):
    def setUp(self):
        self.rot47 = ROT47()

    def test_encrypt_rot47_for_single_word(self):
        before_encrypt1 = "arbuz"
        self.assertEqual(self.rot47.encrypt(before_encrypt1), "2C3FK")

    def test_encrypt_rot47_for_several_words_first_type(self):
        before_encrypt2 = "ptaki lataja kluczem"
        self.assertEqual(self.rot47.encrypt(before_encrypt2), "AE2<: =2E2;2 <=F4K6>")

    def test_encrypt_rot47_for_several_words_second_type(self):
        before_encrypt3 = "project errors"
        self.assertEqual(self.rot47.encrypt(before_encrypt3), "AC@;64E 6CC@CD")

    def test_decrypt_rot47_for_single_word(self):
        before_decrypt1 = "2C3FK"
        self.assertEqual(self.rot47.decrypt(before_decrypt1), "arbuz")

    def test_decrypt_rot47_for_several_words_first_type(self):
        before_decrypt2 = "AE2<: =2E2;2 <=F4K6>"
        self.assertEqual(self.rot47.decrypt(before_decrypt2), "ptaki lataja kluczem")

    def test_decrypt_rot47_for_several_words_second_type(self):
        before_decrypt3 = "AC@;64E 6CC@CD"
        self.assertEqual(self.rot47.decrypt(before_decrypt3), "project errors")
