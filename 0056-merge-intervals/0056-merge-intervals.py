class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if not intervals:
            return []

        ps = intervals[0][0]
        pe = intervals[0][1]
        result = []
        i = 1 
        while i < len(intervals):
            cs = intervals[i][0]
            ce = intervals[i][1]

            if cs <= pe:
                ps = min(ps,cs)
                pe = max(pe,ce)
            else:
                result.append([ps,pe])
                ps = cs
                pe = ce
            i += 1 
            
        result.append([ps,pe])
        
        return result