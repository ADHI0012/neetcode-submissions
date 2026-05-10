class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lookUp = {0:1}
        currSum = 0
        count = 0

        for i in range(n):
            currSum += nums[i]
            if currSum - k in lookUp:
                count += lookUp[currSum - k]

            
            lookUp[currSum] = 1 + lookUp.get(currSum, 0)

        return count
