class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, n + 1):
            aStart, aEnd = res[-1]
            bStart, bEnd = intervals[i]
            if aEnd >= bStart:
                res[-1] = ([aStart, max(aEnd, bEnd)])
            else:
                res.append([bStart, bEnd])

        return res