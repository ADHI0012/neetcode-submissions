class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        look_up = set(nums)
        maxlen = 1

        for num in nums:
            if num - 1 not in look_up:
                l = 1
                target = num
                while target + 1 in look_up:
                    l += 1
                    maxlen = max(maxlen, l)
                    target += 1

        return maxlen