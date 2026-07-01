class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def isValid(t):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= t:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count == p:
                    return True

            return False

        res = 0
        l,r = 0,10**8

        while l <= r:
            mid = (l + r) // 2
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res