import unittest

from src.managers.manager import Manager


class TestManager(unittest.TestCase):
    def setUp(self):
        manager = Manager()

    def test_encrypt_rot13_in_manager(self):
        ...