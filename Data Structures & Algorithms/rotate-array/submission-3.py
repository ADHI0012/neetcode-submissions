class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        res = [0 for _ in range(n)]
        l = 0

        for i in range(n-k, n):
            res[l] = nums[i]
            l += 1

        for i in range(0, n-k):
            res[l] = nums[i]
            l += 1

        for i in range(n):
            nums[i] = res[i]