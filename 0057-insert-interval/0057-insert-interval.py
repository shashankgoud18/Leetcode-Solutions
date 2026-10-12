class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        result = []

        for i,(start,end) in enumerate(intervals):
            if end<newInterval[0]:
                result.append([start,end])
            
            elif start > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            else:
                newInterval[0] = min(newInterval[0],start)
                newInterval[1] = max(newInterval[1],end)
        result.append(newInterval)
        return result