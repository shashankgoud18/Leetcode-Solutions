class Solution:
    def rob(self, nums: list[int]) -> int:
        #Top Down approach
        # n = len(nums)
        # memo = [-1]*n
        # def solve(i):
        #     if i >= n:
        #         return 0 
        #     if memo[i] != -1:
        #         return memo[i]
        #     steal = nums[i] + solve(i+2)
        #     skip = solve(i+1)
        #     memo[i] =  max(steal,skip)
        #     return memo[i]

        # return solve(0)

        #Bottom up approach
        n = len(nums)
        if n == 1:
            return nums[0]
        t = [0]*(n+1)
        t[1] = nums[0]

        for i in range(2,n+1):
            steal = nums[i-1] + t[i-2]
            skip = t[i-1]

            t[i] = max(steal,skip)
        
        return t[n]

