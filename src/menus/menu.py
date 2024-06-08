class Menu:
    def __init__(self, options: dict) -> None:
        self.options: dict = options

    def display(self):
        print(35 * "*")
        for key, value in self.options.items():
            print(f"{key}. {value}")
        print(35 * "*")

    def make_choice(self):
        choice = int(input("Podaj swój wybór: "))
        if not self.is_choice_valid(choice, self.options):
            raise ValueError("Wybór poza zakresem")
        return choice

    @staticmethod
    def is_choice_valid(choice: int, options: dict) -> bool:
        return 1 <= choice <= len(options)
