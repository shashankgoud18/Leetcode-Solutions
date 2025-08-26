class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        hash_map = {}
        for i in range(n):
            if nums[i] in hash_map:
               hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1
        
        smaller = {}
        total = 0
        for i in range(0,101):
            smaller[i] = total
            if i in hash_map:
                total += hash_map[i]
        
        result = []
        for num in nums:
            result.append(smaller[num])
        
        return result
