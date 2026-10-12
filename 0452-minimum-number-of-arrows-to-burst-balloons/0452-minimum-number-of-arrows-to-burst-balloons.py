class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        prev_end = points[0][1]
        for i in range(len(points)):
            start,end = points[i]
            if start > prev_end:
                count += 1
                prev_end = end
            else:
                prev_end = min(prev_end,end)
        return count           