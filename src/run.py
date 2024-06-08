from src.hashers import rot13
from src.hashers.rot13 import ROT13
from src.helpers.text import Text
from src.helpers.memory_buffer import MemoryBuffer

from src.files.file_handler import FileHandler

buf = MemoryBuffer()
text = Text("str", "rot13", "encrypted")
text2 = Text("str", "rot47", "encrypted")
text3 = Text("st1234", "rot13", "encrypted")
list1 = [text, text3, text2]
# buf.add_text(text)
# buf.add_text(text2)
# buf.add_text(text3)

# print(buf.__str__())
# buf.remove_text("st1234")
# print(buf.__str__())

# options = {1: "Szyfrowanie ROT13",
#            2: "Deszyfrowanie ROT13",
#            3: "Szyfrowanie ROT47",
#            4: "Deszyfrowanie ROT47",
#            5: "Wyświetlenie zapisanych danych",
#            6: "Odczyt z pliku",
#            7: "Zapis do pliku",
#            8: "Usuń dane",
#            9: "Wyjście"
#            }
#
# menu = Menu(options=options)
#
# menu.display()

# FileHandler.save_text_to_file(list1, "tested.json")
t1 = {"text": "str", "rot_type": "rot13", "status": "encrypted"}
print(ROT13.is_text_in_rot13_valid("arbuz"))
# print(Text.is_text_from_dict_valid(t1))

# print(FileHandler.read_from_file("test_read.json"))
