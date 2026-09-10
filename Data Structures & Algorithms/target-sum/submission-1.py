class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(index, total):
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (index, total) in cache:
                return cache[(index, total)]

            cache[(index,total)] = dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])
            return cache[(index,total)]
        
        return dfs(0, 0)
            
