import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashMap = defaultdict(list)
        res = []
        
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            hashMap[dist].append([x,y])
        
        hashMap = dict(sorted(hashMap.items()))

        for x in hashMap:
            for y in hashMap[x]:
                if len(res) == k:
                    break
                res.append(y)
            
    
        
        return res