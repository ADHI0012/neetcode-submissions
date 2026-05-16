class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        l, r = 0, n - 1
        i = 0


        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1

        return nums
                

        
        
