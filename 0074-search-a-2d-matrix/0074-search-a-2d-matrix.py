class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = rows*cols - 1 

        while start <= end:
            mid = start + (end-start)//2

            a = mid//cols 
            b  = mid%cols

            if matrix[a][b] == target:
                return True
            elif matrix[a][b] > target:
                end = mid - 1 
            else:
                start = mid + 1 
        return False
            