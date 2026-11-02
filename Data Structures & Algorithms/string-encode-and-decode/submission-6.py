class Solution:
    __KEY = 5
    __SEPARATOR = "çPoMs#$%"
    __IS_NULL = "ISNULL0-4932LKÇM12#@!#"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.__IS_NULL

        encoded = ""

        joined = self.__SEPARATOR.join(strs)

        for letter in joined:
            ciphered = (ord(letter) + self.__KEY) % 255
            encoded += chr(ciphered)

        return encoded

        

    def decode(self, s: str) -> List[str]:
        if s == self.__IS_NULL:
            return []

        decoded = ""

        for letter in s:
            deciphered = (ord(letter) - self.__KEY) % 255
            decoded += chr(deciphered)

        decoded = decoded.split(self.__SEPARATOR)

        return decoded