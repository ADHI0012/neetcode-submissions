class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        res = []

        while i < n:
            correct = nums[i] - 1
            
            if correct < n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        print(nums)

        for i in range(n):
            if i + 1 != nums[i]:
                res.append(i + 1)

        return res
        