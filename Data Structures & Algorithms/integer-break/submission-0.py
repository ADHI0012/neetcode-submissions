class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(1, i):
                l = max(j, dp[j])
                r = max(i - j, dp[i - j])
                dp[i] = max(dp[i], l * r)

        return dp[n]