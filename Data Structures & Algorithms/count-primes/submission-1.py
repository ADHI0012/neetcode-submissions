import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        isPrime = [True for _ in range(n)]
        isPrime[0], isPrime[1] = False, False
        limit = int(math.sqrt(n))

        for i in range(2, limit + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False

        
        count = 0

        for prime in isPrime:
            if prime:
                count += 1

        return count