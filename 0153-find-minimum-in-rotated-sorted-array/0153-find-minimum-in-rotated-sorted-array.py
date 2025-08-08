class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Brute force
        # n = len(nums)
        # min = nums[n-1]
        # for i in range(0,n):
        #     if nums[i] < min:
        #         min = nums[i]
        # return min

        #Optimal
        n = len(nums)
        low = 0 
        high = n-1
        minimum = nums[n-1]
        while low <= high:
            mid = (low+high)//2
            if nums[low]<=nums[mid]:
                 minimum = min(minimum,nums[low])
                 low = mid + 1
            else:
                minimum = min(minimum,nums[mid])
                high = mid - 1
        return minimum 
