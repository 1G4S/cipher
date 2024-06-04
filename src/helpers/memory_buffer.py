from src.hashers.text import Text


class MemoryBuffer:
    def __init__(self) -> None:
        self.buffer: list[Text] = []

    def add_text(self, data: Text) -> None:
        if self.validation(data=data):
            raise ValueError
        
        self.buffer.append(data)

    def remove_text(self, name: str) -> None:
        for text in self.buffer.copy():
            if name == text.text:
                self.buffer.remove(text)

    @staticmethod
    def validation(data: Text) -> bool:
        if (data.rot_type != "rot13" and data.rot_type != "rot47") or (
                data.status != "encrypted" and data.status != "decrypted"
        ):
            return True
        return False

    def __str__(self):
        print(self.buffer)
