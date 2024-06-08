import sys
import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
from src.menus.menu import Menu


class TestMenu(unittest.TestCase):
    _options = {1: ("Szyfrowanie ROT13", 0),
                2: ("Deszyfrowanie ROT13", 0),
                3: ("Szyfrowanie ROT47", 0),
                4: ("Deszyfrowanie ROT47", 0),
                5: ("Wyświetlenie zapisanych danych", 0),
                6: ("Odczyt z pliku", 0),
                7: ("Zapis do pliku", 0),
                8: ("Usuń dane", 0),
                9: ("Wyjście", 0)
                }

    def setUp(self):
        self.menu = Menu(self._options)

    def test_display_in_menu(self):
        expected_display = """***********************************
1. Szyfrowanie ROT13
2. Deszyfrowanie ROT13
3. Szyfrowanie ROT47
4. Deszyfrowanie ROT47
5. Wyświetlenie zapisanych danych
6. Odczyt z pliku
7. Zapis do pliku
8. Usuń dane
9. Wyjście
***********************************
"""

        with patch('sys.stdout', new=StringIO()) as out:
            self.menu.display()
            self.assertEqual(out.getvalue(), expected_display)

    @patch('builtins.input', side_effect=[2])
    def test_make_choice_in_menu_first_value(self, mock_input):
        self.assertEqual(self.menu.make_choice(), 2)

    @patch('builtins.input', side_effect=[9])
    def test_make_choice_in_menu_second_value(self, mock_input):
        self.assertEqual(self.menu.make_choice(), 9)

    @patch('builtins.input', side_effect=[-1])
    def test_make_choice_in_menu_wrong_value(self, mock_input):
        with self.assertRaises(ValueError):
            self.menu.make_choice()

    def test_validation_in_menu_right_value(self):
        self.assertEqual(self.menu.is_choice_valid(4, self._options), True)

    def test_validation_in_menu_wrong_value(self):
        self.assertEqual(self.menu.is_choice_valid(-4, self._options), False)
