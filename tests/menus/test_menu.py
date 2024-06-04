import sys
import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
from src.menus.menu import Menu


class TestMenu(unittest.TestCase):
    _options = {1: "Szyfrowanie ROT13",
                2: "Deszyfrowanie ROT13",
                3: "Szyfrowanie ROT47",
                4: "Deszyfrowanie ROT47",
                5: "Wyświetlenie zapisanych danych",
                6: "Odczyt z pliku",
                7: "Zapis do pliku",
                8: "Usuń dane",
                9: "Wyjście"
                }

    def setUp(self):
        self.menu = Menu(self._options)

    def test_display(self):
        expected_display = """
        ***********************************
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
