import json
import re

from src.hashers.text import Text
from dataclasses import asdict


class FileHandler:

    @staticmethod
    def save_text_to_file(data: list[Text], filename: str) -> None:
        if not FileHandler.is_filename_valid(filename=filename):
            raise ValueError("Filename is not correct. It must end with .json")

        formatted_text_list = []
        formatted_dict = {}
        for d in data:
            if d.is_text_valid():
                formatted_text_list.append(asdict(d))
            else:
                raise ValueError
        formatted_dict['data'] = formatted_text_list

        with open(filename, "w") as file:
            json.dump(formatted_dict, file, indent=4)

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

    @staticmethod
    def is_filename_valid(filename: str) -> bool:
        pattern = re.compile("[A-z0-9]+.json")
        if pattern.match(filename):
            return True
        return False
