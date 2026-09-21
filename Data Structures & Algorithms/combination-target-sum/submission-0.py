class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, arr):
            nonlocal res
            total = sum(arr)
            if i == len(nums):
                return
            if total == target:
                res.append(arr.copy())
                return
            if total > target:
                return


            arr.append(nums[i])
            dfs(i, arr)
            arr.pop()
            dfs(i + 1, arr)
        
        dfs(0, [])
        return res