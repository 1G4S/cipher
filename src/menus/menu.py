class Menu:
    def __init__(self, options: dict) -> None:
        self.options: dict = options

    def display(self):
        print(35 * '*')
        for key, value in self.options.items():
            print(f'{key}. {value}')
        print(35 * '*')

    def make_choice(self):
        pass