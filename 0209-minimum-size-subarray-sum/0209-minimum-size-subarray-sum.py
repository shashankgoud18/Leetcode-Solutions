class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # n = len(nums)
        # min_subarr = float("inf")

        # for i in range(n):
        #     curr_sum = 0
        #     for j in range(i,n):
        #         curr_sum += nums[j]
        #         if curr_sum >= target:
        #             min_subarr = min(min_subarr,j-i+1)
        #             break
        # if min_subarr == float("inf"):
        #     return 0
        
        # return min_subarr


        left = 0
        right = 0
        n = len(nums)
        curr_sum= 0 
        min_len = float("inf")
        while right<n:
            curr_sum += nums[right]

            while curr_sum >= target:
                subarr_len = right-left + 1
                min_len = min(min_len,subarr_len)
                curr_sum -= nums[left]
                left += 1 
            
            right += 1 
        if min_len == float("inf"):
            return 0
        
        return min_len

        