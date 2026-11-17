class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        def minKadane(nums):
            currSum = nums[0]
            minSum = nums[0]
            for i in range(1,len(nums)):
                currSum = min(nums[i],currSum+nums[i])
                minSum = min(currSum,minSum)
            return minSum
        def maxKadane(nums):
            currSum = nums[0]
            maxSum = nums[0]
            for i in range(1,len(nums)):
                currSum = max(nums[i],currSum+nums[i])
                maxSum = max(currSum,maxSum)
            return maxSum
        totalSum = sum(nums)
        minSum = minKadane(nums)
        maxSum = maxKadane(nums)
        circularSum = totalSum - minSum

        if maxSum > 0:
            return max(maxSum,circularSum)
        return maxSum