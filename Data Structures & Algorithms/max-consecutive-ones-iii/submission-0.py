class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones = zeroes = maxones = l = 0

        for r in range(len(nums)):
            if nums[r]:
                ones += 1
            else:
                zeroes += 1

            while (r - l + 1) - ones > k:
                if nums[l]:
                    ones -= 1
                else:
                    zeroes -= 1

                l += 1

            maxones = max(maxones, r - l + 1)

        return maxones