class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mini = nums[0]
        minTotal = nums[0]

        for i in range(1, len(nums)):
            minTotal = min(minTotal + nums[i], nums[i])
            mini = min(mini, minTotal)
        
        maxTotal = nums[0]
        maxi = nums[0]

        for i in range(1, len(nums)):
            maxTotal = max(maxTotal + nums[i], nums[i])
            maxi = max(maxi, maxTotal)
        
        total = sum(nums)
        
        if total == mini:
            return max(nums)
        
        return max(maxi, total - mini)