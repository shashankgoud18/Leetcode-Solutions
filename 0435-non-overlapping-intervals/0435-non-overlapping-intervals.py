class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort()
        n = len(intervals)
        count = 0
        i = 0
        j = 1 

        while j<n:
            current_interval = intervals[i]
            next_interval = intervals[j]

            cs = current_interval[0]
            ce = current_interval[1]
            ns  = next_interval[0]
            ne = next_interval[1]

            if ce <= ns:
                i = j
                j += 1 
            elif ce > ne:
                i = j
                j += 1
                count += 1 
            elif ce <= ne:
                j += 1
                count += 1
        return count

            