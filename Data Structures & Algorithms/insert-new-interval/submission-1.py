class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        for i in range(n):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i,newInterval)
        if len(intervals) == n :
            intervals.append(newInterval)
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1] = [res[-1][0],max(res[-1][1],interval[1])]
        return res
            
        