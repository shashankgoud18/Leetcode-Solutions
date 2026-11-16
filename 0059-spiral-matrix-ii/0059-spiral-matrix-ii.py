class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = n
        top = 0
        bottom = m-1
        left = 0
        right = n-1
        dir = 0
        i = 1
        matrix = [[0]*n for _ in range(n)]
        while top<=bottom and left<=right:

            if dir == 0:#left to right
                for j in range(left,right+1): 
                    matrix[top][j] = i
                    i += 1 
                top += 1 
            elif dir == 1: 
                for j in range(top,bottom+1):
                    matrix[j][right] = i
                    i += 1 
                right -= 1 
            elif dir == 2:
                for j in range(right,left-1,-1):
                    matrix[bottom][j] = i
                    i += 1 
                bottom -= 1
            elif dir == 3:
                for j in range(bottom,top-1,-1):
                    matrix[j][left] = i
                    i += 1 
                left += 1 
            dir += 1 
            if dir == 4:
                dir = 0
        
        return matrix
                 
