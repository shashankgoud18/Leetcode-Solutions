class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<target:
                low = mid+1
            elif nums[mid] == target:
                return mid 
            else:
                high = mid-1
        return -1