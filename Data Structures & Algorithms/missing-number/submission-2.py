class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            correct = nums[i]

            if correct < n and nums[correct] != nums[i]:
                nums[correct], nums[i] = nums[i], nums[correct]
            else:
                i += 1

        for i in range(n):
            if i != nums[i]:
                return i
        return i + 1
