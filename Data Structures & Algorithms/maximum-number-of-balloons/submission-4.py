class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        freq = {}
        count = 0
        min_freq = float('inf')

        for ch in text:
            freq[ch] = 1 + freq.get(ch, 0)

        for ch in "balloon":
            try:
                if ch != "l" and ch != "o":
                    min_freq = min(min_freq, freq[ch])
                else:
                    min_freq = min(min_freq, freq[ch] // 2)
            except KeyError:
                return 0
        return min_freq


        