class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        l = 0
        maxlen = 0

        for i in range(n):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
                

            seen.add(s[i])
            maxlen = max(maxlen, len(seen))

        return maxlen
