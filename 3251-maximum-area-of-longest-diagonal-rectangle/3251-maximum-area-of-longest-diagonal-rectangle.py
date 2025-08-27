class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_diag_sq = 0
        max_area = 0
        for length, width in dimensions:
            diag_sq = length * length + width * width
            area = length * width
            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                max_area = area
            elif diag_sq == max_diag_sq:
                max_area = max(max_area, area)
        return max_area