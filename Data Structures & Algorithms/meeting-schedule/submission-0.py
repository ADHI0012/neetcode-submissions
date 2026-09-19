"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda x: x.start)

        for i in range(n):
            aStart, aEnd = intervals[i].start, intervals[i].end
            for j in range(i + 1, n):
                bStart, bEnd = intervals[j].start, intervals[j].end
                if bStart < aEnd:
                    return False
        
        return True