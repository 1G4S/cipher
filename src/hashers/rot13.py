from src.hashers.cipher import Cipher


class ROT13(Cipher):
    def encrypt(self, text: str) -> str:
        if self.validation(text):
            raise ValueError

        return text.translate(str.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
        ))

    def decrypt(self, text: str) -> str:
        if self.validation(text):
            raise ValueError

        return text.translate(str.maketrans(
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
        ))

    @staticmethod
    def validation(text: str) -> bool:
        return any(str(i) in text for i in range(10))
