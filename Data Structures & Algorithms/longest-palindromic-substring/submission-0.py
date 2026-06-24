class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxlen = 0
        L = R = -1

        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    maxlen = r - l + 1
                    L,R = l,r
                l,r = l - 1, r + 1
            l,r = i, i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxlen:
                    maxlen = r - l + 1
                    L,R = l,r
                l,r = l - 1, r + 1

        return s[L : R + 1]
