class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(i, total):
            if total == amount:
                return 0
            if total > amount or i == len(coins):
                return float('inf')
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            take = 1 + dfs(i, total + coins[i])
            skip = dfs(i + 1, total)

            cache[(i, total)] = min(take, skip)
            return cache[(i, total)]
        
        res = dfs(0,0)
        if res == float('inf'):
            return -1
        
        return res