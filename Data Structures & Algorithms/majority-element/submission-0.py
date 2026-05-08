import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = math.floor(n / 2)
        hashMap = {}

        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)

            if hashMap[num] > majority:
                return num

        