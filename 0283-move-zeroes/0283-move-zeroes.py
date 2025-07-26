class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = []
        for i in range(0,n):
             if nums[i] != 0:
                temp.append(nums[i])
        m = len(temp)
        for i in range(0,m):
            nums[i] = temp[i]
        for i in range(m,n):
            nums[i] = 0
        return nums