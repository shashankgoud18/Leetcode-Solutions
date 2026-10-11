class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        sr = int(c**0.5)
        l = 0
        r = sr
        
        while l <= r:
            sum = l*l + r*r
            if sum < c:
                l += 1 
            elif sum == c:
                return True
            else:
                r -= 1
        return False
            
        