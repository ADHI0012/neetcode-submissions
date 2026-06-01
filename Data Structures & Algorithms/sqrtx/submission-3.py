class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0

        while left <= right:
            mid = (left + (right - left) // 2) # if left and right are too large, to prevent adding them (to avoid overflow)
            value = mid * mid
            if value == x:
                return mid
            elif value < x:
                left = mid + 1
                res = mid
            else:
                right = mid - 1

        return res

            
        