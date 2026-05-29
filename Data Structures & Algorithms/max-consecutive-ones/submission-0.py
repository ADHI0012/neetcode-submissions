class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        ones = 0
        for num in nums:
            if num:
                ones += 1
                maxones = max(ones, maxones)
            else:
                ones = 0

        return maxones
                