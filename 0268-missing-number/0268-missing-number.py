class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        natural_sum = (n*(n+1))//2
        sum = 0
        for i in nums:
            sum += i 
        return natural_sum - sum