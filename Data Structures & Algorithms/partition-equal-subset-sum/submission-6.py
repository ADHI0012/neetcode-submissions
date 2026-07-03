class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        n = len(nums)
        target = total // 2

        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for num in nums:
            for j in range(target, 0, -1):
                if num <= j:
                    dp[j] = dp[j] or dp[j - num]
                        

        return dp[target]

                



        print(dp)
        return dp[target]

