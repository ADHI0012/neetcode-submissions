class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev = nums[0]

        for i in range(1, len(nums)):
                if nums[i] < prev:
                        return nums[i]
                prev = nums[i]

        return nums[0]

        
        