import sys

from src.files.file_handler import FileHandler
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

    def decrypt_rot13(self) -> None:
        text: str = input("Podaj dane, które chcesz odszyfrować: ")
        decrypted_text: str = self.rot13.decrypt(text=text)
        new_text: Text = Text(text=decrypted_text, rot_type="rot13", status="decrypted")
        self.memory.add_text(data=new_text)

    def encrypt_rot47(self) -> None:
        text: str = input("Podaj dane, które chcesz zaszyfrować: ")
        encrypted_text: str = self.rot47.encrypt(text=text)

        new_text: Text = Text(text=encrypted_text, rot_type="rot47", status="encrypted")
        self.memory.add_text(data=new_text)

    def decrypt_rot47(self) -> None:
        text: str = input("Podaj dane, które chcesz odszyfrować: ")
        decrypted_text: str = self.rot47.decrypt(text=text)
        new_text: Text = Text(text=decrypted_text, rot_type="rot47", status="decrypted")
        self.memory.add_text(data=new_text)

    def display_memory_buffer(self) -> None:
        print(self.memory.buffer)

    def read_from_file(self) -> None:
        path: str = input("Podaj ścieżkę do pliku: ")
        data_read = FileHandler.read_from_file(path=path)
        self.memory.add_list_of_texts(data=data_read)

    def save_to_file(self) -> None:
        filename: str = input("Podaj nazwę pliku: ")
        FileHandler.save_text_to_file(data=self.memory.buffer, filename=filename)

    def clear_memory(self) -> None:
        self.memory.buffer = []

    @staticmethod
    def exit_program() -> None:
        sys.exit()
