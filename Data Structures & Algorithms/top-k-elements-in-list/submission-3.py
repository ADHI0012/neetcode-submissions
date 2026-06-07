import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}
        freq = [[] for _ in range(n + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for el in count:
            freq[count[el]].append(el)

        res = []
        
        for i in range(n, 0, -1):
            if freq[i]:
                for j in freq[i]:
                    res.append(j)
                    if len(res) == k:
                        return res

        
        
        


        