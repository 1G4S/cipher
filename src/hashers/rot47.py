from src.hashers.cipher import Cipher


class ROT47(Cipher):
    _enc_dec_table: str = r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

    def encrypt(self, text: str) -> str:
        if self.is_text_in_rot47_valid(text):
            return text.translate(str.maketrans(
                self._enc_dec_table,
                self._enc_dec_table[47:] + self._enc_dec_table[:47]))
        else:
            raise ValueError

    def decrypt(self, text: str) -> str:
        if self.is_text_in_rot47_valid(text):
            return text.translate(str.maketrans(
                self._enc_dec_table[47:] + self._enc_dec_table[:47],
                self._enc_dec_table))
        else:
            raise ValueError

    @staticmethod
    def is_text_in_rot47_valid(text: str) -> bool:
        wrong_chars: str = "ĄąĆćĘęŁłŃńÓóŚśŹźŻż"
        return all(i not in text for i in wrong_chars)
