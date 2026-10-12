import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf') for _ in range(n + 1)]
        distances[0] = float('-inf')
        distances[k] = 0

        for i in range(n):
            for s,d,cost in times:
                newcost = cost + distances[s]
                distances[d] = min(distances[d], newcost)
        
        res = max(distances)
        if res == float('inf'): return -1

        return res
