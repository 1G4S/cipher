import unittest
from src.hashers.rot47 import ROT47


class TestRot47(unittest.TestCase):
    def setUp(self):
        self.rot47 = ROT47()

    def test_encrypt_rot47_for_single_word(self):
        before_encrypt = "arbuz"
        self.assertEqual(self.rot47.encrypt(text=before_encrypt), "2C3FK")

    def test_encrypt_rot47_for_several_words_first_type(self):
        before_encrypt = "ptaki lataja kluczem"
        self.assertEqual(self.rot47.encrypt(text=before_encrypt), "AE2<: =2E2;2 <=F4K6>")

    def test_encrypt_rot47_for_several_words_second_type(self):
        before_encrypt = "project errors"
        self.assertEqual(self.rot47.encrypt(text=before_encrypt), "AC@;64E 6CC@CD")

    def test_decrypt_rot47_for_single_word(self):
        before_decrypt = "2C3FK"
        self.assertEqual(self.rot47.decrypt(text=before_decrypt), "arbuz")

    def test_decrypt_rot47_for_several_words_first_type(self):
        before_decrypt = "AE2<: =2E2;2 <=F4K6>"
        self.assertEqual(self.rot47.decrypt(text=before_decrypt), "ptaki lataja kluczem")

    def test_decrypt_rot47_for_several_words_second_type(self):
        before_decrypt = "AC@;64E 6CC@CD"
        self.assertEqual(self.rot47.decrypt(text=before_decrypt), "project errors")

    def test_validation_in_rot_47_for_wrong_value(self):
        text_to_validate = "ąrbóz"
        self.assertEqual(ROT47.validation(text=text_to_validate), True)

    def test_validation_in_rot_47_for_right_value(self):
        text_to_validate = "arbuz-012:"
        self.assertEqual(ROT47.validation(text=text_to_validate), False)