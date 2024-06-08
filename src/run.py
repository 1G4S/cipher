from src.hashers import rot13
from src.hashers.rot13 import ROT13
from src.helpers.text import Text
from src.helpers.memory_buffer import MemoryBuffer

from src.files.file_handler import FileHandler
from src.menus.menu import Menu

# buf = MemoryBuffer()
# text = Text("str", "rot13", "encrypted")
# text2 = Text("str", "rot47", "encrypted")
# text3 = Text("st1234", "rot13", "encrypted")
# list1 = [text, text3, text2]
# buf.add_text(text)
# buf.add_text(text2)
# buf.add_text(text3)
#
# print(buf.__str__())
# buf.remove_text("st1234")
# print(buf.__str__())

options = {1: ("Szyfrowanie ROT13", "ROT13"),
           2: ("Deszyfrowanie ROT13", "Deszt"),
           3: ("Szyfrowanie ROT47", "1231"),
           4: ("Deszyfrowanie ROT47", "sada"),
           5: ("Wyświetlenie zapisanych danych", "sadas"),
           6: ("Odczyt z pliku", "asdas"),
           7: ("Zapis do pliku", "sadas"),
           8: ("Usuń dane", "asdad"),
           9: ("Wyjście", "asda")
           }

menu = Menu(options=options)

menu.display()

# FileHandler.save_text_to_file(list1, "tested.json")
t1 = {"text": "str", "rot_type": "rot13", "status": "encrypted"}
