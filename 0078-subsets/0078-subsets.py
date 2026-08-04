class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        i = 0
        def solve(i,subset,nums):
            if i == len(nums):
                ans.append(subset[:]) 
                return

            subset.append(nums[i])
            solve(i+1,subset,nums)

            subset.pop()
            solve(i+1,subset,nums)
        
        solve(0,subset,nums)
        
        return ans

