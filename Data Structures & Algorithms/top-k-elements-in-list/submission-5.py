class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        res = []
        for num in nums:
            freq[num] += 1
        
        freq = dict(sorted(freq.items(), reverse=True,key=lambda x: x[1]))


        for i in freq:
            res.append(i)
            if len(res) == k:
                return res