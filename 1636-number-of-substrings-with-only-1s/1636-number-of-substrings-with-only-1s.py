class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        count = 0
        curr = int(s[0])
        mod = 10**9 + 7
        for i in range(1,n):
            if s[i] == '1':
                curr += 1 
            else:
                count += (curr*(curr+1))//2
                curr = 0
        
        count += (curr*(curr+1))//2
        return count % mod