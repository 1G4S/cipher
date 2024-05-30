from __future__ import annotations
from abc import ABC, abstractmethod


class Cipher(ABC):
    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass
