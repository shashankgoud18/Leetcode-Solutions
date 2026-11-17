class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        def kadanesMin(nums):
            currSum = nums[0]
            minSum = nums[0]

            for i in range(1,len(nums)):
                currSum = min(nums[i],currSum+nums[i])
                minSum = min(currSum,minSum)
            return minSum
        def kadanesMax(nums):
            currSum = nums[0]
            maxSum = nums[0]

            for i in range(1,len(nums)):
                currSum = max(nums[i],currSum+nums[i])
                maxSum = max(currSum,maxSum)
            return maxSum

        minSum = kadanesMin(nums)
        maxSum = kadanesMax(nums)

        if abs(minSum) > abs(maxSum):
            return abs(minSum)
        return abs(maxSum)