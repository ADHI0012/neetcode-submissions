class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if nums[i] < 0:
                i += 1
                continue
            correct = nums[i] - 1
            if correct > n - 1:
                i += 1
                continue
            print(correct)

            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        print(nums)

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1

        