class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookUp = set(nums)
        maxRange = 0

        for num in nums:
            rangeLen = 1

            if num - 1 not in lookUp:
                for i in range(1,len(nums)):
                    if num + i in lookUp:
                        rangeLen += 1
                    else:
                        break
            maxRange = max(maxRange, rangeLen)

        return maxRange