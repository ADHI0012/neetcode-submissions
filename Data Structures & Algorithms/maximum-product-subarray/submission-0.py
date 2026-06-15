class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_pdt = float('-inf')

        for i in range(n):
            pdt = 1
            for j in range(i, n):
                pdt *= nums[j]
                max_pdt = max(max_pdt, pdt)

        return max_pdt