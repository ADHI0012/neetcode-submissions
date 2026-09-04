class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        res = []
        def bfs(i,j):
            q = collections.deque()
            visited = set()
            q.append((i,j))
            visited.add((i,j))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            pacific = atlantic = False

            if i == 0 or j == 0:
                pacific = True
            if i == rows - 1 or j == cols - 1:
                atlantic = True
            
            if pacific and atlantic:
                return True
            
            while q:
                size = len(q)
                for _ in range(size):
                    r,c = q.popleft()
                    if r == 0 or c == 0:
                        pacific = True
                    if r == rows - 1 or c == cols - 1:
                        atlantic = True

                    for m,n in directions:
                        row = r + m
                        col = c + n
                        cond = row < 0 or row >= rows or col < 0 or col >= cols
                        if cond or heights[row][col] > heights[r][c] or (row,col) in visited:
                            continue
                        q.append((row,col))
                        visited.add((row,col))

            return pacific and atlantic


        for i in range(rows):
            for j in range(cols):
                if bfs(i,j):
                    res.append([i,j])
            
        return res