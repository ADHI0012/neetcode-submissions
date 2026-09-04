class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()


        def bfs():
            steps = 1
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            while q:
                size = len(q)
                for _ in range(size):
                    r,c = q.popleft()
                    for m,n in directions:
                        row = r + m
                        col = c + n
                        cond = row < 0 or col < 0 or row >= rows or col >= cols

                        if cond or grid[row][col] == -1 or (row,col) in visited:
                            continue

                        grid[row][col] = steps
                        q.append((row,col))
                        visited.add((row,col))
                steps += 1


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        bfs()

        