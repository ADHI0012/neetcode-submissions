class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, prev):
            if i == len(nums):
                return 0
            # if i == len(nums) - 1:
            #     return 1
            if (i, prev) in cache:
                return cache[(i, prev)]
            if prev is None:
                take = 1 + dfs(i + 1, nums[i])
            elif prev != None and prev < nums[i]:
                take = 1 + dfs(i + 1, nums[i])
            else:
                take = float('-inf')
            
            skip = dfs(i + 1, prev)

            cache[(i, prev)] = max(take, skip)
            return cache[(i, prev)]

        return dfs(0, None)