import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        heap = []

        for i in s:
            freq[i] = 1 + freq.get(i, 0)
            
        
        
        res = ""


        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))
        
        prev = None
        
        while heap:
            count, ch = heapq.heappop(heap)
            count = abs(count)
            res += ch
            if prev is not None and abs(prev[0]) > 0:
                heapq.heappush(heap, prev)
            prev = (-(count-1), ch)

        return res if len(res) == len(s) else ""

