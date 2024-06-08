from src.helpers.text import Text


class MemoryBuffer:
    def __init__(self) -> None:
        self.buffer: list[Text] = []

    def add_text(self, data: Text) -> None:
        if not self.is_data_valid(data=data):
            raise ValueError

        self.buffer.append(data)

    def remove_text(self, name: str) -> None:
        self.buffer = [text for text in self.buffer if name != text.text]

    @staticmethod
    def is_data_valid(data: Text) -> bool:
        if (data.rot_type == "rot13" or data.rot_type == "rot47") and (
                data.status == "encrypted" or data.status == "decrypted"
        ):
            return True
        return False

    def __str__(self):
        return self.buffer
