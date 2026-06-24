class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            l = r = i
            while l >= 0 and r < n:
                print(l,r)
                if s[l] == s[r]:
                    count += 1
                else:
                    break
                l,r = l - 1, r + 1
            l,r = i,i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    count += 1
                else:
                    break
                l,r = l - 1, r + 1

        return count
    

        