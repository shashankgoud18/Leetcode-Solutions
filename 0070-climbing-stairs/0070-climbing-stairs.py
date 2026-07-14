class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)

        def helper(n,dp):
            if n == 0:
                return 1 
            if n == 1:
                return 1 
            if dp[n] != -1:
                return dp[n]

            left = helper(n-1,dp)
            right = helper(n-2,dp)

            dp[n] = left + right

            return dp[n]
        
        return helper(n,dp)
