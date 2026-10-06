class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # """
        # candidate = None
        # count = 0 

        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     if num == candidate:
        #         count += 1 
        #     else:
        #         count -= 1 
        # return candidate
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num,0)+1

        n = len(nums) 
        for key,val in hmap.items():
            if val > n//2:
                return key
            