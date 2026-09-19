class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n =len(intervals)
        # if n == 1:
        #     return intervals
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, n):
            aStart, aEnd = res[-1]
            bStart, bEnd = intervals[i]

            if aEnd >= bStart:
                res[-1] = [aStart, max(aEnd, bEnd)]
            else:
                res.append([bStart, bEnd])
        return res
