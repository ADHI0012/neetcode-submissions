import math, heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, [-dist, x, y])

            if len(heap) > k:
                heapq.heappop(heap)

        for point in heap:
            res.append([point[1], point[2]])

        return res

