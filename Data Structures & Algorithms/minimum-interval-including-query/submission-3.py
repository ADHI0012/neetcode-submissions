import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        queries = [(q, i) for i,q in enumerate(queries)]
        queries.sort()
        res = [-1 for _ in range(len(queries))]

        i = 0
        j = 0
        heap = []
        while j < len(queries):
            while i < len(intervals) and queries[j][0] >= intervals[i][0]:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while heap and heap[0][1] < queries[j][0]:
                heapq.heappop(heap)
            index = queries[j][1]
            res[index] = heap[0][0] if heap else -1
            j += 1
        return res

# [1,2,3,6,7,8]