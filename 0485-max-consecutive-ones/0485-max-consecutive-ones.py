class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0 
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1 
            else:
                result = max(curr,result)
                curr = 0
        result = max(curr,result)
        
        return result