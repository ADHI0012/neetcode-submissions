class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(l,r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l,r = l + 1, r - 1
            
            return True

        n,count = len(s),0

        for i in range(n):
            for j in range(i,n):
                if is_palindrome(i, j):
                    count += 1
                

        return count
        