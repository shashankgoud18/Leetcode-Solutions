class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        
        n = len(position)

        def possible(midForce):
            prev = position[0]
            countBalls = 1
            for i in range(1,n):
                curr = position[i]
                if curr - prev >= midForce:
                    countBalls += 1
                    prev = curr
                if countBalls == m:
                    break
            return countBalls == m
                
            

        position.sort()
        minForce = 1
        maxForce = position[-1] - position[0]
        result = 0

        while minForce <= maxForce:
            midForce = minForce + (maxForce-minForce)//2
            if possible(midForce):
                result = midForce
                minForce = midForce+1
            else:
                maxForce = midForce - 1 
        
        return result
