class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0

        while left <= right:
            mid = (left + right) // 2
            value = mid * mid
            if value == x:
                return mid
            elif value < x:
                left = mid + 1
                res = mid
            else:
                right = mid - 1

        return res

            
        