class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        total = 0
        largest = float('-inf')

        for num in nums:
            if num > largest:
                largest = num
            total += num
        
        def isValid(mid):
            total = 0
            count = 1
            for num in nums:
                if num + total > mid:
                    count += 1
                    total = num
                else:
                    total += num
            
            return count <= k
        
        l,r = largest, total
        res = 0

        while l <= r:
            mid = (l + r) // 2
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res


