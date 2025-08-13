class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        result = []
        hash_map = {}
        for i in range(n):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1
        for key in hash_map:
            if hash_map[key] > n/3:
                result.append(key)
        return result