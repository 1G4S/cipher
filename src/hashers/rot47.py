from src.hashers.cipher import Cipher


class ROT47(Cipher):
    def encrypt(self, text: str) -> str:
        rot47_text = r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        return text.translate(str.maketrans(
            rot47_text,
            rot47_text[47:] + rot47_text[:47]))

    def decrypt(self, text: str) -> str:
        rot47_text = r"""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        return text.translate(str.maketrans(
            rot47_text[47:] + rot47_text[:47],
            rot47_text))
