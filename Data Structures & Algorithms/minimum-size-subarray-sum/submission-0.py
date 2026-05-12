class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        l = 0
        n = len(nums)
        currSum = 0

        for r in range(n):
            currSum += nums[r]
            while currSum >= target:
                minlen = min(r - l + 1, minlen)
                currSum -= nums[l]
                l += 1
            


        if minlen == float('inf'):
            minlen = 0
        
        return minlen
