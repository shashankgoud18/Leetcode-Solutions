class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        final = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                final = max(count,final)
            else:
                count = 0
        return final