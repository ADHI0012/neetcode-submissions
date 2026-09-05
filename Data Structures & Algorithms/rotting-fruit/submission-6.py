class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        q = collections.deque()
        visited = set()
        fresh_count = 0

        def bfs():
            nonlocal fresh_count
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            minutes = 0

            while q:
                size = len(q)
                for _ in range(size):
                    r,c = q.popleft()
                    for m,n in directions:
                        row = r + m
                        col = c + n
                        cond = row < 0 or row >= rows or col < 0 or col >= cols

                        if cond or grid[row][col] == 0 or (row, col) in visited:
                            continue
                        
                        q.append((row,col))
                        visited.add((row,col))
                        fresh_count -= 1
                if q:        
                    minutes += 1
            
            return minutes if fresh_count == 0 else -1
                        



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        minutes = bfs()

        return minutes