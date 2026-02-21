class Solution:
    def isPrime(self,n):
        if n==1:
            return False
        if n==2:
            return True
        if n%2==0:
            return False
        
        i = 3 
        while i*i <= n:
            if n%i==0:
                return False
            i+= 2 
        return True
    
    def countBits(self,n):
        count = 0
        while n:
           n = n & (n - 1)
           count += 1
        return count
            

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left,right+1):

            bitCount = self.countBits(i)
            checkPrime = self.isPrime(bitCount)
            if checkPrime:
                count += 1
            else:
                continue
        
        return count