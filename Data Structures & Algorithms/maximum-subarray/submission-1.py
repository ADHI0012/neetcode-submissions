class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')

        for i in range(len(nums)):
            windowSum = 0
            for j in range(i, len(nums)):
                windowSum += nums[j]
                maxSum = max(windowSum, maxSum)

        return maxSum