class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        target = len(cost)
        globalC = float('inf')
        cache = {}
        def dfs(i,c):
            nonlocal globalC
            if i == target:
                globalC = min(globalC, c)
                return globalC
            if i > target:
                return 0
            
            if (i,c) in cache:
                return cache[(i,c)]
            
            cache[(i,c)] = min(dfs(i + 1, c + cost[i]),
            dfs(i + 2, c + cost[i]))
            return cache[(i,c)]
        
        dfs(0,0)
        dfs(1, 0)
        return globalC