class Solution(object):
    def findDuplicate(self, nums):

        for num in nums:
            index = abs(num)

            if nums[index] < 0:
                return index

            else:
                nums[index] *= -1

    
                
        