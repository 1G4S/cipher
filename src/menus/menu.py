from typing import Callable


class Menu:
    def __init__(self, options: dict[int, tuple[str, Callable]]) -> None:
        self.options: dict = options

    def display(self) -> None:
        print(35 * "*")
        for key, value in self.options.items():
            print(f"{key}. {value[0]}")
        print(35 * "*")

    def make_choice(self):
        choice = int(input("Podaj swój wybór: "))
        if not self.is_choice_valid(choice, self.options):
            raise ValueError("Choice is out of range.")
        return choice

    @staticmethod
    def is_choice_valid(choice: int, options: dict) -> bool:
        return 1 <= choice <= len(options)

    def update_options(self, options: dict[int, tuple[str, Callable]]) -> None:
        self.options = options
