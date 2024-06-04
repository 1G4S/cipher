from src.hashers.text import Text
from src.helpers.memory_buffer import MemoryBuffer
from src.menus.menu import Menu

buf = MemoryBuffer()
text = Text('str', 'rot13', 'encrypted')
text2 = Text('str', 'rot47', 'encrypted')
text3 = Text('st1234', 'rot13', 'encrypted')
buf.add_text(text)
buf.add_text(text2)
buf.add_text(text3)

# print(buf.__str__())
# buf.remove_text("st1234")
# print(buf.__str__())

options = {1: "Szyfrowanie ROT13",
           2: "Deszyfrowanie ROT13",
           3: "Szyfrowanie ROT47",
           4: "Deszyfrowanie ROT47",
           5: "Wyświetlenie zapisanych danych",
           6: "Odczyt z pliku",
           7: "Zapis do pliku",
           8: "Usuń dane",
           9: "Wyjście"
           }

menu = Menu(options=options)

menu.display()