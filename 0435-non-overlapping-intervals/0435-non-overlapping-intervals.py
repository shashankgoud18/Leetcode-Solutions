class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        result = [intervals[0]]
        count = 0
        for i in range(1,len(intervals)):
            start,end = intervals[i][0],intervals[i][1]

            if result[-1][1] <= start:
                result.append([start,end])
            else:
                count += 1 
        
        return count

