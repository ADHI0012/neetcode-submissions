class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        res = [0 for _ in range(n)]

        i = n - 1

        while l <= r:
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]

            if left > right:
                res[i] = left
                l += 1
            else:
                res[i] = right
                r -= 1
            i -= 1
        
        return res