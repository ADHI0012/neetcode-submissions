class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        count = 0
        odd = False
        for i in s:
            freq[i] = 1 + freq.get(i, 0)


        print(freq)

        for ch in freq:
            if freq[ch] % 2:
                count += freq[ch] - 1
                odd = True
            else:
                count += freq[ch]

        return count + 1 if odd else count


# M A L A Y A L A M

