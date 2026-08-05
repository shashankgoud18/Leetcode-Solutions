class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        subset = []
        i = 0

        def solve(i,subset,nums):
            if i == len(nums):
                if subset in ans:
                    return
                ans.append(subset[:])
                return

            subset.append(nums[i])
            solve(i+1,subset,nums)

            subset.pop()
            solve(i+1,subset,nums)

             


        solve(i,subset,nums)
        return ans


