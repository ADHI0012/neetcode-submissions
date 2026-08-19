class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        minutes = 0
        fresh_count = 0

        def bfs():
            nonlocal minutes
            nonlocal fresh_count
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            while q:
                size = len(q)
                for _ in range(size):
                    r,c = q.popleft()
                    for m,n in directions:
                        row = r + m
                        col = c + n

                        if (0 <= row < rows and 0 <= col < cols and grid[row][col] == 1):
                            visited.add((row,col))
                            q.append((row,col))
                            grid[row][col] = 2
                            fresh_count -= 1
                minutes += 1



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0

        bfs()

        return minutes - 1 if fresh_count == 0 else -1
