class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_map = {}
        n = len(nums)
        for i in range(0,n):
            if nums[i] in hash_map:
                 hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
        for key in hash_map:
            if hash_map[key] >= 2:
                return True
            
        return False