class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse = 0
        num = n
        while num>0:
            ld =  num%10
            reverse = reverse*10 + ld
            num = num//10
        
        return abs(n-reverse)