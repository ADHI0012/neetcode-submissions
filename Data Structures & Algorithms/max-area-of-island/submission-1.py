class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        maxArea = 0
        
        def bfs(i,j):
            q.append((i,j))
            visited.add((i,j))
            cells = 0
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            while q:
                size = len(q)
                for _ in range(size):
                    r,c = q.popleft()
                    cells += 1

                    for m,n in directions:
                        row = r + m
                        col = c + n
                        cond = row < 0 or col < 0 or row >= rows or col >= cols
                        if cond or (row, col) in visited or grid[row][col] == 0:
                            continue
                        q.append((row,col))
                        visited.add((row,col))
            return cells

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = bfs(i, j)
                    maxArea = max(area, maxArea)
        return maxArea