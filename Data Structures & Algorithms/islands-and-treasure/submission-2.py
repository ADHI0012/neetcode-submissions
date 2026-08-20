class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()


        def bfs():
            directions = [[1,0], [0,1], [-1,0],[0,-1]]
            steps = 1
            while q:
                size = len(q)
                for _ in range(size):
                    r,c = q.popleft()
                    if grid[r][c] == INF:
                        grid[r][c] = steps
                        continue
                    for m,n in directions:
                        row = r + m
                        col = c + n
                        condition = row < 0 or col < 0 or row >= rows or col >= cols
                        if condition or grid[row][col] == -1 or (row,col) in visited:
                            continue
                        if grid[row][col] == INF:
                            grid[row][col] = steps
                            visited.add((row,col))
                            q.append((row,col))
                    
                steps += 1
                        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))

        bfs()
