class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
       
        def reverse(nums, L, R):
            l = L
            r = R - 1

            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(nums, 0, n)
        reverse(nums, 0, k)
        reverse(nums, k, n)
        