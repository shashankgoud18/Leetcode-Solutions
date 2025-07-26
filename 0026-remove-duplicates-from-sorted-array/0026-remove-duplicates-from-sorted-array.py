class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq_map = {}
        for i in range(0,n):
            freq_map[nums[i]] = 0 
        
        freq_map = sorted(freq_map)
        j = 0
        for k in freq_map:
            nums[j] = k
            j+=1
        return j

        

        