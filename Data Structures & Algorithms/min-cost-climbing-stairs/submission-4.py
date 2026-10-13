class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}

        def dfs(i):
            if i >= len(cost):
                return 0
            
            if i in cache:
                return cache[i]
            
            cost1 = cost[i] + dfs(i + 1)
            cost2 = float('inf')
            if i + 2 <= len(cost):
                cost2 = cost[i] + dfs(i + 2)

            cache[i] = min(cost1, cost2)
            return cache[i]

        dfs(0)
        return min(cache[0], cache[1])