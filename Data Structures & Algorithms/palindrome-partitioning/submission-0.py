class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, path):
            if i == len(s):
                res.append(path[:])
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    path.append(s[i:j+1])
                    dfs(j + 1, path)
                    path.pop()
        
        dfs(0,[])
        return res