class Solution:
    def isUgly(self, n: int) -> bool:
        prime_factors = []
        d = 2
        if n <= 0: 
            return False

        while d * d <= n:
            if n % d == 0:
                prime_factors.append(d)
                while n % d == 0:
                    n = n // d
            d += 1
        

        if n > 1:
            prime_factors.append(n)
        
        for num in prime_factors:
            if num != 2 and num != 3 and num != 5:
                return False
        
        return True
        