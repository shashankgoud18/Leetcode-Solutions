class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix) #row
        n = len(matrix[0]) #cols

        dir = 0 #left to right
        # dir = 1 #top to bottom
        # dir = 2 #right to left
        # dir = 3 #bottom to top

        top = 0
        down = m-1
        left = 0
        right = n-1
        result = []

        while top<=down and left<=right:
            if dir == 0:
                #constant row --> top
                for i in range(left,right+1):
                    result.append(matrix[top][i])

                top += 1 
            if dir == 1:
                #constant col --> right
                for i in range(top,down+1):
                    result.append(matrix[i][right])
                right -= 1 
            if dir == 2:
                #constant row --> bottom
                for i in range(right,left-1,-1):
                    result.append(matrix[down][i])
                down -= 1 
            if dir == 3:
                #constant col --> left
                for i in range(down,top-1, -1):
                    result.append(matrix[i][left])
                left += 1
            
            dir += 1 
            if dir == 4:
                dir = 0
            
        return result
