class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],-x[1]))
        n = len(intervals)
        max_ending = 0
        count = 0
        for i in range(n):
            current_interval = intervals[i]
            cs = current_interval[0]
            ce = current_interval[1]

            if ce > max_ending:
                max_ending = max(ce,max_ending)
                continue
            else:
                count += 1
        return n - count