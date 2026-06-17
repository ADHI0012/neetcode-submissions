class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_prefix = 0
        prefix = 0
        max_sum = nums[0]

        for i in range(len(nums)):
            prefix += nums[i]
            max_sum = max(max_sum, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)

        return max_sum