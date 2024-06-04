from src.hashers.text import Text


class MemoryBuffer:
    def __init__(self) -> None:
        self.buffer: list[Text] = []

    def add_text(self, data: Text) -> None:
        self.buffer.append(data)

    def remove_text(self, name: str) -> None:
        for text in self.buffer.copy():
            if name == text.text:
                self.buffer.remove(text)

    def __str__(self):
        print(self.buffer)
