class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        min_sum = float('inf')
        curr = 0

        for num in nums:
            if curr > 0:
                curr = num
            else:
                curr += num
            min_sum = min(min_sum, curr)

        wrapped = total_sum - min_sum
        unwrapped = float('-inf')
        curr = 0

        for num in nums:
            if curr < 0:
                curr = num
            else:
                curr += num
            unwrapped = max(unwrapped, curr)

        if unwrapped < 0: return unwrapped

        return max(unwrapped, wrapped)


