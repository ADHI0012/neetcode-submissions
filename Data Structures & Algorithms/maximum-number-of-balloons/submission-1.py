class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        freq = {}
        count = 0

        for ch in text:
            freq[ch] = 1 + freq.get(ch, 0)

        while True:
            for ch in s:
                if ch not in freq or freq[ch] == 0:
                    return count
                else:
                    freq[ch] -= 1
            count += 1

        