class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        visited = [False] * len(nums)

        def dfs(path, visited):
            if len(path) == len(nums):
                temp = tuple(path)
                res.add(temp)

            for j in range(len(nums)):
                if not visited[j]:
                    path.append(nums[j])
                    visited[j] = True
                    dfs(path, visited)
                    path.pop()
                    visited[j] = False
        
        dfs([], visited)
        return [list(i) for i in res]