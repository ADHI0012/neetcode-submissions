class Solution:
    def isUgly(self, n: int) -> bool:
        factors = [2,3,5]

        if n <= 0:
            return False


        for d in factors:
            while n % d == 0:
                n = n // d
        
        return n == 1