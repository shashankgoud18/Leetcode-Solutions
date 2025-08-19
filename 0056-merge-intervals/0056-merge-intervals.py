class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        result = [intervals[0]]
        start = 0
        end = 1
        for i in range(1,len(intervals)):
            curr = intervals[i]
            last = result[-1]
            if curr[start]<=last[end]:
                minimum = min(curr[start],last[start])
                maximum = max(curr[end],last[end])
                result[-1] = [minimum,maximum]
            else:
                temp = curr
                result.append(temp)
        return result