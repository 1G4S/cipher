import unittest
from src.hashers.rot13 import ROT13


class TestRot13(unittest.TestCase):
    def setUp(self):
        self.rot13 = ROT13()

    def test_encrypt_rot13_for_single_word(self):
        before_encrypt = "arbuz"
        self.assertEqual(self.rot13.encrypt(text=before_encrypt), "neohm")

    def test_encrypt_rot13_for_several_words_first_type(self):
        before_encrypt = "ptaki lataja kluczem"
        self.assertEqual(
            self.rot13.encrypt(text=before_encrypt), "cgnxv yngnwn xyhpmrz"
        )

    def test_encrypt_rot13_for_several_words_second_type(self):
        before_encrypt = "project errors"
        self.assertEqual(self.rot13.encrypt(text=before_encrypt), "cebwrpg reebef")

    def test_decrypt_rot13_for_single_word(self):
        before_decrypt = "neohm"
        self.assertEqual(self.rot13.decrypt(text=before_decrypt), "arbuz")

    def test_decrypt_rot13_for_several_words_first_type(self):
        before_decrypt = "cgnxv yngnwn xyhpmrz"
        self.assertEqual(
            self.rot13.decrypt(text=before_decrypt), "ptaki lataja kluczem"
        )

    def test_decrypt_rot13_for_several_words_second_type(self):
        before_decrypt = "cebwrpg reebef"
        self.assertEqual(self.rot13.decrypt(text=before_decrypt), "project errors")

    def test_validation_in_rot_13_for_wrong_value(self):
        text_to_validate = "1ąr3buz2"
        self.assertEqual(ROT13.validation(text=text_to_validate), True)

    def test_validation_in_rot_13_for_right_value(self):
        text_to_validate = "arbuz"
        self.assertEqual(ROT13.validation(text=text_to_validate), False)
