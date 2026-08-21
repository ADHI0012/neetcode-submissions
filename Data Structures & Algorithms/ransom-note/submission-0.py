class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        for s in magazine:
            freq[s] = 1 + freq.get(s, 0)
        
        for s in ransomNote:
            if s not in freq or freq[s] == 0:
                return False
            freq[s] -= 1
        
        return True
            
        
