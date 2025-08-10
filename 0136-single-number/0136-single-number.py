class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Brute Force
        # hash_map = {}
        # for num in nums:
        #     if num in hash_map:
        #         hash_map[num] += 1
        #     else:
        #         hash_map[num] = 1
        
        # for key in hash_map:
        #     if hash_map[key]==1:
        #         return key
        

        #optimal
        ans = 0
        for num in nums:
            ans = ans^num
        return ans