class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum <=0:
                maxSum = max(sum,maxSum)
                sum = 0
                continue
            maxSum = max(sum,maxSum)
        
        return maxSum