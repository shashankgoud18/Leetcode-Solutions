class Solution(object):
    def lowerBound(self,nums,target):
        n = len(nums)
        low = 0
        high = n-1
        lb = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                lb = mid
                high = mid-1 
            else:
                low = mid + 1
        return lb

    def upperBound(self,nums,target):
        n = len(nums)
        low = 0
        high = n-1
        ub = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] > target:
                ub = mid
                high = mid-1 
            else:
                low = mid + 1
        return ub


    def searchRange(self, nums, target):
        lb = self.lowerBound(nums,target)
        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        ub = self.upperBound(nums,target)
        last_pos = ub - 1 if ub != -1 else len(nums) - 1

        return [lb,last_pos]