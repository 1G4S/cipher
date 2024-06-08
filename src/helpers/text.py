from dataclasses import dataclass


@dataclass
class Text:
    text: str
    rot_type: str
    status: str

    def is_text_valid(self) -> bool:
        if (self.rot_type == "rot13" or self.rot_type == "rot47") and (
                self.status == "encrypted" or self.status == "decrypted"
        ):
            return True
        return False

    @staticmethod
    def is_text_from_dict_valid(data: dict) -> bool:
        if (data["rot_type"] == "rot13" or data["rot_type"] == "rot47") and (
                data["status"] == "encrypted" or data["status"] == "decrypted"
        ):
            return True
        return False

    @staticmethod
    def from_dict(data: dict) -> "Text":
        if not Text.is_text_from_dict_valid(data=data):
            raise ValueError
        return Text(**data)
