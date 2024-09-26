import random


class EncryptMsg:
    CHARS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    def __init__(self, key):
        if not self.is_valid_key(key):
            raise ValueError("Invalid key")

        self.key_list = self._key_to_list(key)

    @classmethod
    def is_valid_key(cls, key: str):
        key_set = set(key.lower())
        char_set = set(cls.CHARS)

        res = char_set.intersection(key_set)
        if len(res) == len(cls.CHARS):
            return True

        return False

    def _key_to_list(self, key: str):
        return list(key.lower())

    @classmethod
    def _random_char(cls):
        index = random.randint(0, len(cls.CHARS) - 1)
        return cls.CHARS[index]

    @classmethod
    def create_key(cls):
        key_set: set = set()

        for i in range(len(cls.CHARS)):
            char = cls._random_char()
            while char in key_set:
                char = cls._random_char()
            key_set.add(char)

        return "".join(key_set)

    def _is_valid_char(self, char: str):
        if char in self.CHARS:
            return True
        return False

    def encrypt(self, message: str):
        msg_list = list(message.lower())

        encrypted = ""

        for char in msg_list:
            if not self._is_valid_char(char):
                encrypted += char
                continue
            index = self.CHARS.index(char)
            encrypted += self.key_list[index]

        return encrypted

    def decrypt(self, message: str):
        msg_list = list(message.lower())

        decrypted = ""

        for char in msg_list:
            if not self._is_valid_char(char):
                decrypted += char
                continue
            index = self.key_list.index(char)
            decrypted += self.CHARS[index]

        return decrypted
