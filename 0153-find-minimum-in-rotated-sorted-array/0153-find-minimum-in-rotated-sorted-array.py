class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min = nums[n-1]
        for i in range(0,n):
            if nums[i] < min:
                min = nums[i]
        return min