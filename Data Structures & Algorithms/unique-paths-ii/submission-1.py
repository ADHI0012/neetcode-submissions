class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        dp[m - 1][n - 1] = 1

        for i in range(m - 2, -1, -1):
            if obstacleGrid[i][n - 1] == 1:
                dp[i][n-1] = 0
            else:
                dp[i][n-1] = dp[i + 1][n-1]
        
        for i in range(n - 2, -1, -1):
            if obstacleGrid[m - 1][i] == 1:
                dp[m-1][i] = 0
            else:
                dp[m-1][i] = dp[m-1][i + 1]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]