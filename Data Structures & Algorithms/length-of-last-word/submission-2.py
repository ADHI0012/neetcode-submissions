class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1
        length,r = 0,len(s) - 1
        while s[r] == " ":
            r -= 1
        while s[r] != ' ':
            length += 1
            r -= 1
        
        return length