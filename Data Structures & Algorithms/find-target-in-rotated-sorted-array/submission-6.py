class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(l,r):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return -1

        l,r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        r = len(nums) - 1
        

        if nums[pivot] <= target <= nums[r]:
            return binary_search(pivot, r)
        else:
            return binary_search(0, pivot - 1)

