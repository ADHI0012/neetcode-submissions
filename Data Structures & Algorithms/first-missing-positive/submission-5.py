class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n,i = len(nums), 0

        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
                continue

            correct = nums[i] - 1
            if nums[correct] != nums[i]:
                nums[correct], nums[i] = nums[i], nums[correct]
            else:
                i += 1

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1
