class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        window = set()

        for i in range(len(nums)):
            if i - l > k:
                window.remove(nums[l])
                l += 1

            if nums[i] in window:
                return True

            window.add(nums[i])

        return False