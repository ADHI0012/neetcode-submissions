class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        freqCount = {}
        maxlen = 0

        for r in range(n):
            freqCount[s[r]] = 1 + freqCount.get(s[r], 0)
            while (r - l + 1) - max(freqCount.values()) > k:
                freqCount[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)

        return maxlen
            
            
