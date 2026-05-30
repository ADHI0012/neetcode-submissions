class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False
        last = nums[0]

        for i in range(1, len(nums)):
            if increasing and decreasing:
                return False
            if nums[i] < last:
                decreasing = True
                last = nums[i]
            elif nums[i] > last:
                increasing = True
                last = nums[i]

        return not (increasing and decreasing)
            
        