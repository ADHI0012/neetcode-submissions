import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        cost = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

        for u,v,time in times:
            adj[u].append(v)
            cost[u][v] = time
            
        distances = [float('inf') for _ in range(n + 1)]
        distances[0] = float('-inf')
        distances[k] = 0
        heap = [(0,k)]

        while heap:
            dist, node = heapq.heappop(heap)

            for x in adj[node]:
                newcost = dist + cost[node][x]
                if distances[x] > newcost:
                    distances[x] = newcost
                    heapq.heappush(heap, (distances[x], x))
        
        res = max(distances)
        if res == float('inf'): return -1
        return res
