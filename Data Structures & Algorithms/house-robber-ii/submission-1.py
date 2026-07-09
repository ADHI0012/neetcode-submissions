class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        DP = [0 for _ in range(n)]

        DP[1] = nums[1]

        for i in range(2, n):
            DP[i] = max(DP[i - 2] + nums[i], DP[i - 1])

        return max(DP[n - 1], dp[n - 2])