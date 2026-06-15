class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_pdt = float("-inf")
        prefix = suffix = 1
        res = nums[0]

        for i in range(n):
            prefix *= nums[i]
            suffix *= nums[n - 1 - i]
            res = max(max(prefix, suffix), res)

            prefix = 1 if prefix == 0 else prefix
            suffix = 1 if suffix == 0 else suffix

        return res
