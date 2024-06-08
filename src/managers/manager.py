from src.hashers.rot13 import ROT13
from src.hashers.rot47 import ROT47
from src.helpers.memory_buffer import MemoryBuffer
from src.helpers.text import Text


class Manager:
    def __init__(self):
        self.memory = MemoryBuffer()
        self.rot13 = ROT13()
        self.rot47 = ROT47()

    def encrypt_rot13(self) -> None:
        text: str = input("Podaj dane, które chcesz zaszyfrować: ")
        encrypted_text: str = self.rot13.encrypt(text=text)

        new_text: Text = Text(text=encrypted_text, rot_type="rot13", status="encrypted")
        self.memory.add_text(data=new_text)




