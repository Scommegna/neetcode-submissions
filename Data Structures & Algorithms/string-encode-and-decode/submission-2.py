class Solution:
    separator = "|:|"
    rotation_value = 3
    empty = "__EMPTY__"

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.empty

        joined_strs = self.separator.join(strs)

        encoded = ""

        for letter in joined_strs:
            encoded += "".join(chr(ord(letter) + self.rotation_value))

        return encoded

    def decode(self, s: str) -> List[str]:
        if s == self.empty:
            return []

        decrypted = ""

        for c in s:
            decrypted += "".join(chr(ord(c) - self.rotation_value))

        return decrypted.split(self.separator)