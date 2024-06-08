class Menu:
    def __init__(self, options: dict) -> None:
        self.options: dict = options

    def display(self):
        print(35 * '*')
        for key, value in self.options.items():
            print(f'{key}. {value}')
        print(35 * '*')

    def make_choice(self):
        try:
            choice = int(input("Podaj swój wybór: "))
            if self.validation(choice, self.options):
                raise ValueError('Wybór poza zakresem')
            return choice
        except ValueError as e:
            print(f'Błąd: {e}')

    @staticmethod
    def validation(choice: int, options: dict) -> bool:
        return not (1 <= choice <= len(options))