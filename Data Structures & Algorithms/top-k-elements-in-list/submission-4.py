class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        res = []
        for num in nums:
            freq[num] += 1
        
        bucket = [[] for _ in range(n + 1)]
        
        for num, occ in freq.items():
            bucket[occ].append(num)
        
        for i in range(n, -1, -1):
            if bucket[i]:
                for j in bucket[i]:
                    res.append(j)
                    if len(res) == k:
                        return res
        
