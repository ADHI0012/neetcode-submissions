class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dfs(i, j):
            if j == len(s):
                return True
            if i == len(t):
                return False
            
            if t[i] == s[j]:
                return dfs(i + 1, j + 1)
            
            return dfs(i + 1, j)
        
        return dfs(0 ,0)