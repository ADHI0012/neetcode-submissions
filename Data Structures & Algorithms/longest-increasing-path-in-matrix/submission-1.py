class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        cache = {}
        def dfs(i, j, prev):
            if i >= rows or j >= cols or i < 0 or j < 0:
                return 0
            if (i, j, prev) in cache:
                return cache[(i, j, prev)]
            if prev != None and matrix[i][j] > prev:
                p = matrix[i][j]
                cache[(i, j, prev)] = 1 + max(dfs(i + 1, j, p), dfs(i, j + 1, p), dfs(i - 1, j, p), dfs(i, j - 1, p))
            else:
                # return max(dfs(i + 1, j, prev), dfs(i, j + 1, prev), dfs(i - 1, j, prev), dfs(i, j - 1, prev))
                cache[(i, j, prev)] = 0
            return cache[(i, j, prev)]
        
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j, matrix[i][j] - 1))
        
        return res
            
