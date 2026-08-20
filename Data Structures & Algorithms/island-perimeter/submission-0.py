class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visited = set()
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])

        def bfs(i,j):
            nonlocal perimeter
            visited.add((i,j))
            q.append((i,j))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            while q:
                r,c = q.popleft()
                cell_perimeter = 4
                
                
                for m,n in directions:
                    row = r + m
                    col = c + n
                    if row < 0 or col < 0 or row >= rows or col >= cols:
                        continue
                    if grid[row][col] == 0:
                        continue
                    cell_perimeter -= 1
                    if (row,col) not in visited:
                        visited.add((row,col))
                        q.append((row,col))

                perimeter += cell_perimeter 

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    bfs(i,j)
        
        return perimeter
                    


