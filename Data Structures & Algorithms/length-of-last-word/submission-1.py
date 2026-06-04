class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 1:
            return 1
        length,r = 0,len(s) - 1
        while s[r] != ' ':
            length += 1
            r -= 1
        
        return length