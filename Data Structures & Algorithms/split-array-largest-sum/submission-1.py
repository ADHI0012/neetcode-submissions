class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        maxi = float('-inf')
        total = 0

        for num in nums:
            if num > maxi:
                maxi = num
            total += num
        
        lower, upper = maxi, total
        res = 0

        def isValid(ans):
            count = 1
            tot = 0

            for num in nums:
                if num + tot > ans:
                    count += 1
                    tot = num
                else:
                    tot += num
            
            return count <= k




        while lower <= upper:
            mid = (lower + upper) // 2
            if isValid(mid):
                res = mid
                upper = mid - 1
            else:
                lower = mid + 1
        
        return res


