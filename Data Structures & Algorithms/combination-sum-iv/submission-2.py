class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mini = min(nums)
        if target == 0: return 1
        if mini > target: return 0

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        dp[mini] = 1

        for i in range(mini + 1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] = dp[i] + dp[i - num]

        print(dp)
        return dp[target]