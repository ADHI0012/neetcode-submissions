class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        res = []
        
        def dfs(path, visited):
            if len(path) == len(visited):
                res.append(path[:])
                return

            for j in range(len(nums)):
                if not visited[j]:
                    path.append(nums[j])
                    visited[j] = True
                    dfs(path, visited)
                    path.pop()
                    visited[j] = False
        dfs([],visited)
        return res

