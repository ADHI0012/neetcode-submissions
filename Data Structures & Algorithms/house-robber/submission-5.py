class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}

        def dfs(i, total):
            if i >= len(nums):
                return total
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            take = dfs(i + 2, total + nums[i])
            skip = dfs(i + 1, total)

            cache[(i, total)] = max(take, skip)
            return cache[(i, total)]
        
        return dfs(0,0)