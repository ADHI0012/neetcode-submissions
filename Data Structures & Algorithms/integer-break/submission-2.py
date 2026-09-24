class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [float('-inf') for _ in range(n + 1)]
        # dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(i):
                left = max(j, dp[j])
                right = max(i - j, dp[i-j])

                dp[i] = max(dp[i], left * right)
        print(dp)
        return dp[n]