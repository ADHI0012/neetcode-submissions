class Solution:
    def lengthOfLIS(self, nums):
        cache = {}
        
        def dfs(i, prev):
            if i == len(nums):
                return 0

            if (i,prev) in cache:
                return cache[(i,prev)]            
            skip = dfs(i + 1, prev)
            take = float('-inf')

            if nums[i] > prev:
                take = 1 + dfs(i + 1, nums[i])
            cache[(i,prev)] = max(take, skip)
            return cache[(i,prev)]
        
        return dfs(0,float('-inf'))