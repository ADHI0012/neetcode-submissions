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

        for i in range(1, n):
            aStart, aEnd = intervals[i - 1].start, intervals[i - 1].end
            bStart, bEnd = intervals[i].start, intervals[i].end

            if aEnd > bStart:
                return False
        
        return True