class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        n = len(nums)
        target = total // 2
        cache = {}

        def dfs(i, total):
            if total == target:
                return True
            if i == len(nums):
                return False
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)
            return cache[(i, total)]
    
        return dfs(0,0)
        
