class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        j = 0
        while j < len(s):
            length = ""
            while s[j] != "#":
                length += s[j]
                j += 1
            length = int(length)
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            j = j + length + 1

        return res