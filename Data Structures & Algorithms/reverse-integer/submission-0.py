class Solution:
    def reverse(self, x: int) -> int:

        res = 0
        temp = x
        temp = -temp if x < 0 else temp

        while temp != 0:
            res = res * 10 + temp % 10
            temp = temp // 10

        res = -res if x < 0 else res

        if res < -2**31 or res > 2**31 - 1:
            return 0

        return res

