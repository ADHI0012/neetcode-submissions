class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        q = collections.deque()
        visited = set()
        cannot_touch = set()

        def bfs(i,j,flag):
            if flag:
                cannot_touch.add((i,j))
            else:
                board[i][j] = "X"
            visited.add((i,j))
            q.append((i,j))
            directions = [[1,0], [0,1], [-1,0], [0,-1]]

            while q:
                r,c = q.popleft()
                for m,n in directions:
                    row = r + m
                    col = c + n

                    if (row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visited or board[row][col] == "X"):
                        continue
                    if flag:
                        cannot_touch.add((row,col))
                    else:
                        board[row][col] = "X"
                    q.append((row, col))
                    visited.add((row,col))



        for i in range(cols):
            if board[0][i] == "O":
                bfs(0,i,1)
        for i in range(cols):
            if board[rows - 1][i] == "O":
                bfs(rows - 1, i,1)
        for i in range(rows):
            if board[i][0] == "O":
                bfs(i,0,1)
        for i in range(rows):
            if board[i][cols - 1] == "O":
                bfs(i, cols - 1,1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in visited and (i,j) not in cannot_touch:
                    bfs(i,j,0)
        

            

        