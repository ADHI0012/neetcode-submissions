class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        temp = n
        n = -n if n < 0 else n
        while n:
            res = res * x
            n -= 1

        return (1 / res) if temp < 0 else res
