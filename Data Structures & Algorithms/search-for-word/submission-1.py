class Solution:
    def exist(self, board, word):
        m,n = len(board),len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if r >= m or c >= n or r < 0 or c < 0 or (r,c) in path or board[r][c] != word[i]:
                return False
            
            path.add((r,c))
            res = dfs(r + 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r,c))
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        
        return False