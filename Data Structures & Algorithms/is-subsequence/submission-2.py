class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cache = {}
        def dfs(i, j):
            if j == len(s):
                return True
            if i == len(t):
                return False
            
            if (i, j) in cache:
                return cache[(i,j)]
            
            if t[i] == s[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i,j)]
        
        return dfs(0 ,0)