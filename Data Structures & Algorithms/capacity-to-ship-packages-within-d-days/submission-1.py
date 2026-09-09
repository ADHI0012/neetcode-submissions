class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)
        res = 0

        def isValid(ans):
            day = 1
            tot = 0
            for num in weights:
                if tot + num > ans:
                    day += 1
                    tot = num
                else:
                    tot += num
            
            return not day > days

        while l <= r:
            mid = (l + r) // 2

            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
