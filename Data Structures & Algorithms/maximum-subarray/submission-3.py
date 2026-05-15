class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxCrossingSum(arr, l, r, mid):
            leftSum = float('-inf')
            currSum = 0

            for i in range(mid, l-1, -1):
                currSum += arr[i]
                if currSum > leftSum:
                    leftSum = currSum
            
            rightSum = float('-inf')
            currSum = 0

            for i in range(mid + 1, r+1):
                currSum += arr[i]
                if currSum > rightSum:
                    rightSum = currSum

            return leftSum + rightSum

        def maxSubArray(arr, l, r):
            if l == r:
                return arr[r]

            mid = (l + r) // 2

            leftSum = maxSubArray(arr, l, mid)
            rightSum = maxSubArray(arr, mid + 1, r)
            crossSum = maxCrossingSum(arr, l, r, mid)

            return max(leftSum, rightSum, crossSum)

        return maxSubArray(nums,0,len(nums) - 1)
            