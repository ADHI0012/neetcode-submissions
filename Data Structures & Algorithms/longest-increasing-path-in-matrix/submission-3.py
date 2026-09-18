class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        cache = {}
        def dfs(i, j, prev):
            if i >= rows or j >= cols or i < 0 or j < 0 or matrix[i][j] <= prev:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if prev != None and matrix[i][j] > prev:
                p = matrix[i][j]
                cache[(i, j)] = 1 + max(dfs(i + 1, j, p), dfs(i, j + 1, p), dfs(i - 1, j, p), dfs(i, j - 1, p))
            return cache[(i, j)]
        
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j, matrix[i][j] - 1))
        
        return res
            
