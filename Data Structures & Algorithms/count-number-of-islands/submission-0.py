from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        islands = 0


        def bfs(i, j):
            nonlocal q
            visited.add((i, j))
            q.append((i, j))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            
            while q:
                r,c = q.popleft()
                for m, n in directions:
                    row = r + m
                    col = c + n
                    if (row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] == "0"):
                        continue
                    q.append((row, col))
                    visited.add((row, col))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands