import json
from src.hashers.text import Text


class FileHandler:

    @staticmethod
    def save_text_to_file(data: Text, filename: str) -> None:
        if FileHandler.validation(data):
            raise ValueError

        formatted_data: dict = {
            "text": data.text,
            "rot_type": data.rot_type,
            "status": data.status,
        }
        with open(filename, "w") as file:
            json.dump(formatted_data, file)

    @staticmethod
    def read_from_file(path: str) -> Text:
        with open(path) as file:
            data: dict = json.load(file)

        text: Text = Text(data["text"], data["rot_type"], data["status"])
        if FileHandler.validation(data=text):
            raise ValueError
        return text

    @staticmethod
    def validation(data: Text) -> bool:
        if (data.rot_type != "rot13" and data.rot_type != "rot47") or (
            data.status != "encrypted" and data.status != "decrypted"
        ):
            return True
        return False
