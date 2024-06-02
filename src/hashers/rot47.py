from src.hashers.cipher import Cipher


class ROT47(Cipher):
    _enc_dec_table: str = r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

    def encrypt(self, text: str) -> str:
        if self.validation(text):
            raise ValueError

        return text.translate(str.maketrans(
            self._enc_dec_table,
            self._enc_dec_table[47:] + self._enc_dec_table[:47]))

    def decrypt(self, text: str) -> str:
        if self.validation(text):
            raise ValueError
        
        return text.translate(str.maketrans(
            self._enc_dec_table[47:] + self._enc_dec_table[:47],
            self._enc_dec_table))

    @staticmethod
    def validation(text: str) -> bool:
        wrong_chars: str = "ĄąĆćĘęŁłŃńÓóŚśŹźŻż"
        return any(i in text for i in wrong_chars)
