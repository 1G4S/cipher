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

    def remove_text(self, index: int) -> None:
        if not MemoryBuffer.is_choice_valid(index, self.buffer):
            raise ValueError("Choice is out of range.")
        del self.buffer[index - 1]

    @staticmethod
    def is_choice_valid(choice: int, buffer: list) -> bool:
        return 1 <= choice <= len(buffer) - 1

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
