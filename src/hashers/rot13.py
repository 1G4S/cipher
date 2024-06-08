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
        if not self.is_text_in_rot13_valid(text):
            raise ValueError
        return text.translate(self._enc_table)

    def decrypt(self, text: str) -> str:
        if not self.is_text_in_rot13_valid(text):
            raise ValueError
        return text.translate(self._dec_table)

    @staticmethod
    def is_text_in_rot13_valid(text: str) -> bool:
        wrong_chars: str = "ĄąĆćĘęŁłŃńÓóŚśŹźŻż0123456789"
        return all(i not in text for i in wrong_chars)
