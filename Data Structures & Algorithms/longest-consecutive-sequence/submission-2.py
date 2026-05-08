class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookUp = set(nums)
        maxRange = 0

        for num in nums:
            rangeLen = 1

            if num - 1 not in lookUp:
                while rangeLen + num in lookUp:
                    rangeLen += 1
            maxRange = max(maxRange, rangeLen)

        return maxRange