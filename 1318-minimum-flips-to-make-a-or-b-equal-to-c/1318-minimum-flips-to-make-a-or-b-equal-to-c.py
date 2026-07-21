class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        
        while a!=0 or b!=0 or c!=0:
            ar = a&1
            br = b&1 
            cr = c&1 

            if cr == 1:
                if ar==0 and br==0:
                    count +=1 
            else:
                count += ar + br
            
            a = a>>1
            b = b>>1
            c = c>>1
        
        return count