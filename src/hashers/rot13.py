from src.hashers.cipher import Cipher


class ROT13(Cipher):
    _enc_table = str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
    )
    _dec_table = str.maketrans(
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    )

    def encrypt(self, text: str) -> str:
        if self.validation(text):
            raise ValueError

        return text.translate(self._enc_table)

    def decrypt(self, text: str) -> str:
        if self.validation(text):
            raise ValueError

        return text.translate(self._dec_table)

    @staticmethod
    def validation(text: str) -> bool:
        return any(str(i) in text for i in range(10))
