class Solution(object):
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        i = 0
        def solve(i,subset,nums):
            if i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            solve(i+1,subset,nums)

            subset.pop()
            solve(i+1,subset,nums)
        solve(0,subset,nums)
        
        return res

        