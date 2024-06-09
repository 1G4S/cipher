from dataclasses import dataclass


@dataclass
class Text:
    text: str
    rot_type: str
    status: str

    def is_text_valid(self) -> bool:
        return self.__is_valid(self.rot_type, self.status)

    @staticmethod
    def is_text_from_dict_valid(data: dict[str, str]) -> bool:
        return Text.__is_valid(data.get("rot_type"), data.get("status"))

    @staticmethod
    def __is_valid(rot_type: str, status: str) -> bool:
        return rot_type in {"rot13", "rot47"} and status in {"encrypted", "decrypted"}

    @staticmethod
    def from_dict(data: dict) -> "Text":
        if not Text.is_text_from_dict_valid(data=data):
            raise ValueError
        return Text(**data)

    def __str__(self):
        return f"Text: {self.text}, Type: {self.rot_type}, Status: {self.status}"
