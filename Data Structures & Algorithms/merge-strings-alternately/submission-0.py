class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0

        p = 0
        res = ""

        while l != len(word1) and r != len(word2):
            if not p % 2:
                res += word1[l]
                l += 1
            else:
                res += word2[r]
                r += 1
            p += 1

        for i in range(l, len(word1)):
            res += word1[i]
        for i in range(r, len(word2)):
            res += word2[i]

        return res 