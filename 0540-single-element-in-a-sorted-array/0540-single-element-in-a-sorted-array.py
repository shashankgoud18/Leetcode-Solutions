class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lb = 0 
        hb = n-1
        while lb < hb:
            mid = (lb+hb)//2
            if mid%2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                lb = mid+2
            else:
                hb = mid
        return nums[lb]
           
        