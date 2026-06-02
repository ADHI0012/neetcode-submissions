class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(nums[l], res)
                break 

            mid = (l + (r - l) // 2)

            if nums[mid] < res:
                res = nums[mid]

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return res

        
        