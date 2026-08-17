from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(i, j):
            nonlocal max_area
            visited.add((i, j))
            q.append((i, j))
            area = 1
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            while q:
                r, c = q.popleft()
                for m, n in directions:
                    row = r + m
                    col = c + n

                    if (row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0 or (row, col) in visited):
                        continue
                    q.append((row, col))
                    visited.add((row, col))
                    area += 1
            max_area = max(max_area, area)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i,j)
        return max_area
        