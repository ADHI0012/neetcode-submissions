class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def getCount(s):
            freq = {}
            for ch in s:
                freq[ch] = 1 + freq.get(ch, 0)
            return freq

        freq1 = getCount(s)
        freq2 = getCount(t)

        for ch in freq2:
            if ch not in freq1 or freq1[ch] != freq2[ch]:
                return ch
