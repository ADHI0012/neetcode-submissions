import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        def isValid(k):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/k)
            
            return not hours > h
    
        l,r = 1,max(piles)

        while l <= r:
            mid = (l + r) // 2
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return res
            
        

        
        
            
