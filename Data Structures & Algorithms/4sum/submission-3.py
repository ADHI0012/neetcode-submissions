class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        nums.sort()
        def dfs(i, curr, total):
            if len(curr) > 4: return
            if total == target and len(curr) == 4:
                res.append(curr[:])
                return
            if i == len(nums):
                return
            
            curr.append(nums[i])
            dfs(i + 1, curr, total + nums[i])
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, curr, total)

        dfs(0,[],0)
        return res