class Solution:
    def rob(self, nums: list[int]) -> int:
        #Top Down
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        
        # def solve(i,n):
        #     if i >= n:
        #         return 0
        #     if t[i] != -1:
        #         return t[i] 
        #     steal = nums[i] + solve(i+2,n)
        #     skip = solve(i+1,n)

        #     t[i] = max(steal,skip)
        #     return t[i]
        # t = [-1]*n
        # take_0th_index = solve(0,n-1)
        # t = [-1]*n
        # take_1st_index = solve(1,n)

        # return max(take_0th_index,take_1st_index)


        #Bottom Up approach
        n = len(nums)
        if n == 1:
            return nums[0]
        t = [0]*n
        t[0] = 0
        
        for i in range(1,n):
            take = nums[i-1] + t[i-2]
            skip = t[i-1]
            t[i] = max(take,skip)
        result = t[n-1]
        print(t)
        t = [0]*(n+1)
        t[0] = 0
        t[1] = 0
        for i in range(2,n+1):
            take = nums[i-1] + t[i-2]
            skip = t[i-1]
            t[i] = max(take,skip)
        print(t)
        result2 = t[n]

        return max(result,result2)