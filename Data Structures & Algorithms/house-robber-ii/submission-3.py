class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        cache = {}
        def dfs(i, total, nums):
            if i >= len(nums):
                return total
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = max(dfs(i + 2, total + nums[i], nums), dfs(i + 1, total, nums))
            return cache[(i, total)]
        
        res1 = dfs(0,0,nums[:n - 1])
        cache = {}
        res2 = dfs(0,0,nums[1:])

        return max(res1, res2)