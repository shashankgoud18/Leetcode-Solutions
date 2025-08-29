class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(0,len(nums)):
            remaining = target-nums[i]
            if remaining in hash_map:
                return [hash_map[remaining],i]
            else:
                hash_map[nums[i]] = i