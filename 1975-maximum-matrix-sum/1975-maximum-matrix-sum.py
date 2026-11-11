class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        count = 0
        m = len(matrix)
        n = len(matrix[0])
        total_sum = 0
        smallest = float("inf")
        for i in range(m):
            for j in range(n):
                if matrix[i][j] < 0:
                    count += 1 
                total_sum += abs(matrix[i][j])
                smallest = min(abs(matrix[i][j]),smallest)
        if count%2 == 0:
            return total_sum
        return total_sum - 2*smallest


                