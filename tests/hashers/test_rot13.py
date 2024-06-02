import unittest
from src.hashers.rot13 import ROT13


class TestRot13(unittest.TestCase):
    def setUp(self):
        self.rot13 = ROT13()

    def test_encrypt_rot13(self):
        before_encrypt1 = "arbuz"
        before_encrypt2 = "ptaki lataja kluczem"
        before_encrypt3 = "project errors"

        self.assertEqual(self.rot13.encrypt(text=before_encrypt1), "neohm")
        self.assertEqual(
            self.rot13.encrypt(text=before_encrypt2), "cgnxv yngnwn xyhpmrz"
        )
        self.assertEqual(self.rot13.encrypt(text=before_encrypt3), "cebwrpg reebef")

    def test_decrypt_rot13(self):
        before_decrypt1 = "neohm"
        before_decrypt2 = "cgnxv yngnwn xyhpmrz"
        before_decrypt3 = "cebwrpg reebef"

        self.assertEqual(self.rot13.decrypt(text=before_decrypt1), "arbuz")
        self.assertEqual(
            self.rot13.decrypt(text=before_decrypt2), "ptaki lataja kluczem"
        )
        self.assertEqual(self.rot13.decrypt(text=before_decrypt3), "project errors")
