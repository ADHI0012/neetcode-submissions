class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        res = []

        def dfs(i, curr):
            if len(curr) > k:
                return
            if i == len(nums):
                if len(curr) == k:
                    res.append(curr[:])
                return
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)
        
        dfs(0,[])
        return res