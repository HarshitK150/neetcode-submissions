from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "_" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        curr_len = ""
        while i < len(s):
            while s[i] != "_":
                curr_len += s[i]
                i += 1

            i += 1
            decoded.append(s[i:i + int(curr_len)])
            i += int(curr_len)
            curr_len = ""
        return decoded