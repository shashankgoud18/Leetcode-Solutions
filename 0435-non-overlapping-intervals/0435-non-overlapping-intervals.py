class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            start,end = intervals[i][0],intervals[i][1]

            if prev_end <= start:
                prev_end = end
            else:
                count += 1 
        
        return count

