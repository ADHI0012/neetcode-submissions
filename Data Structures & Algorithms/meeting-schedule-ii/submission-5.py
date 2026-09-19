"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n <= 1: return n
        intervals.sort(key=lambda x: x.start)
        heap = []
        rooms = 1
        heapq.heappush(heap, intervals[0].end)

        for i in range(1, n):
            start = intervals[i].start
            end = intervals[i].end
            if start >= heap[0]:
                heapq.heappop(heap)
            else:
                rooms += 1
            heapq.heappush(heap, end)
        
        return rooms
