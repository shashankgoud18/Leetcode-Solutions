class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x:x[1])
        arrow = points[0][1]
        count = 1
        i = 1
        while i < len(points):
            if arrow >= points[i][0]:
                i += 1
                continue
            arrow = points[i][1]
            count += 1 
            i += 1
        return count