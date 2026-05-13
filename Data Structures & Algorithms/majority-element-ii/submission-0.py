class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        majority = n // 3
        res = set()
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

            if freq[num] > majority:
                res.add(num)

        return list(res)