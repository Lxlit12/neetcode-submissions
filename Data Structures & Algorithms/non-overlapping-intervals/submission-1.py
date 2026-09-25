class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[1])
        removed = 0
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start < prev_end:
                removed += 1
            else:
                prev_end = end
        return removed