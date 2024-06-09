from src.helpers.text import Text


class MemoryBuffer:
    def __init__(self) -> None:
        self.buffer: list[Text] = []

    def add_text(self, data: Text) -> None:
        if not self.is_data_valid(data=data):
            raise ValueError("Data are not correct.")

        self.buffer.append(data)

    def add_list_of_texts(self, data: list[Text]):
        for d in data:
            if not self.is_data_valid(data=d):
                raise ValueError("Data are not correct.")
            self.buffer.append(d)

    def remove_text(self, name: str) -> None:
        self.buffer = [text for text in self.buffer if name != text.text]

    @staticmethod
    def is_data_valid(data: Text) -> bool:
        if (data.rot_type == "rot13" or data.rot_type == "rot47") and (
                data.status == "encrypted" or data.status == "decrypted"
        ):
            return True
        return False

    def display_memory(self) -> None:
        for count, item in enumerate(self.buffer, 1):
            print(f'{count}. {item}')
