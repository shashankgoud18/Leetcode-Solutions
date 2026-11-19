class Solution:
    def numDecodings(self, s: str) -> int:
        
        def solve(i,n):
            if t[i] != -1:
                return t[i]
            if i == n:
                t[i] = 1
                return t[i]
            if s[i]=='0':
                t[i] = 0
                return t[i]
            
            result1 = solve(i+1,n)
            result2 = 0

            if i+1 < n:
                if s[i] == '1' or s[i]=='2' and s[i+1] <= '6':
                    result2 = solve(i+2,n)

            t[i] = result1 + result2
            return t[i]
        
        n = len(s)
        t = [-1]*(n+1)
        return solve(0,n)