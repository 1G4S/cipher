class Saver:
    @staticmethod
    def save_text_to_file(text: str, filename: str) -> None:
        with open(filename, "w") as file:
            file.write(text)
