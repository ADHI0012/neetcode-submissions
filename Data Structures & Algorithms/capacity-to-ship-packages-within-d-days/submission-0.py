class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights),sum(weights)

        def isValid(capacity):
            i = 0
            d = 0
            n = len(weights)
            while True:
                c = 0
                if i >= n:
                    break
                while i < n and c + weights[i] <= capacity:
                    c += weights[i]
                    i += 1
                d += 1
            
            return d <= days
        
        res = 0

        while l <= r:
            mid = (l + r) // 2
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
