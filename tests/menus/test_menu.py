import unittest
from unittest.mock import patch, MagicMock
from src.menus.menu import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()
    # musze przekazac dict z funkcjami do klasy Menu, potem zamokowac te funkcje magic mock. czyli self.menu.dict['1'] = MagicMock
    # i sprawdzamu czy ta funkcja sie wywolala
    @patch('builtins.input', side_effect=['1'])
    def test_display_menu_option1(self, mock_input):
        pass
