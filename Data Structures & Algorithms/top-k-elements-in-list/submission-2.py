import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap, res = [], []
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for el in freq:
            heapq.heappush(heap, (-freq[el],el))

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        
        
        


        