class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        memo = [-1]*n
        def solve(nums,i):
            if i >= n:
                return 0 
            if memo[i] != -1:
                return memo[i]
            steal = nums[i] + solve(nums,i+2)
            skip = solve(nums,i+1)
            memo[i] =  max(steal,skip)
            return max(memo)

        return solve(nums,0)
