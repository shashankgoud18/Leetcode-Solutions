from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        time = 0
        fresh = 0
        for i in range(m):

            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        
        
        while q:
            is_orange_rotten = False
            for _ in range(len(q)):
                i,j = q.popleft()
                if i>0 and grid[i-1][j]== 1:
                    is_orange_rotten = True
                    grid[i-1][j] = 2
                    q.append((i-1,j))
                    fresh -= 1
            
                if i<m-1 and grid[i+1][j]== 1:
                    is_orange_rotten = True
                    grid[i+1][j] = 2
                    q.append((i+1,j))
                    fresh -= 1
                
                if j>0 and grid[i][j-1]==1:
                    is_orange_rotten = True
                    grid[i][j-1] = 2
                    q.append((i,j-1))
                    fresh -= 1
    
                if j<n-1 and grid[i][j+1]== 1:
                    is_orange_rotten = True
                    grid[i][j+1] = 2
                    q.append((i,j+1))
                    fresh -= 1
    

            if is_orange_rotten:
                time += 1
        if fresh > 0:
            return -1
        
        return time
