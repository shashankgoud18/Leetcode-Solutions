class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        half = n//2
        hash_map = {}
        for i in range(0,n):
            num = nums[i]
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        for k in hash_map:
            if hash_map[k] > half:
                return k
