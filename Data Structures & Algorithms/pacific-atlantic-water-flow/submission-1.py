class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights), len(heights[0])
        pacific = collections.deque()
        atlantic = collections.deque()
        res = []

        def bfs(q,ocean):
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            while q:
                size = len(q)
                for _ in range(size):
                    r,c = q.popleft()
                    ocean.add((r,c))
                    for m,n in directions:
                        row = r + m
                        col = c + n
                        cond = row < 0 or row >= rows or col < 0 or col >= cols

                        if cond or heights[row][col] < heights[r][c] or (row,col) in ocean:
                            continue
                        q.append((row,col))
                        ocean.add((row,col))
                

        


        for i in range(rows):
            pacific.append((i,0))
            atlantic.append((i,cols-1))
        for i in range(cols):
            pacific.append((0,i))
            atlantic.append((rows-1,i))

        pac, atl = set(), set()

        bfs(pacific, pac)
        bfs(atlantic, atl)

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res
