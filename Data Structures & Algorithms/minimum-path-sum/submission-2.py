class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        tot = grid[m - 1][n - 1]

        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = tot + grid[i][n - 1]
            tot += grid[i][n-1]
        
        tot = grid[m - 1][n - 1]

        for i in range(n - 2, -1, -1):
            dp[m - 1][i] = tot + grid[m - 1][i]
            tot += grid[m-1][i]
        
        print(dp)


       
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = min(grid[i][j] + dp[i][j + 1], grid[i][j] + dp[i + 1][j])
        
        return dp[0][0] if dp[0][0] != float('inf') else grid[0][0]
            