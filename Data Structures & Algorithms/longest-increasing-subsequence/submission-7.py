class Solution:
    def lengthOfLIS(self, nums):
        def binary_search(arr, target):
            l,r = 0,len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        temp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                idx = binary_search(temp, nums[i])
                temp[idx] = nums[i]
        
        return len(temp)