class Solution:
    def romanToInt(self, s: str) -> int:
        lookUp = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        n = len(s)
        i = 0

        while i <= n - 1:
            before = s[i]
            if i + 1 <= n - 1:
                after = s[i + 1]
            if i + 1 <= n - 1 and lookUp[before] < lookUp[after]:
                total += (lookUp[after] - lookUp[before])
                i += 2
            else:
                total += lookUp[before]
                i += 1
        return total