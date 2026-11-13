class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True

        # return False

        r = 0
        c = len(matrix[0])-1

        while r<len(matrix) and c>=0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1 
            else:
                r += 1 
        return False

