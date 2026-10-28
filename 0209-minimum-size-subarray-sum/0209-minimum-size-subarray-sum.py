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
        max_length = float("inf")
        total = 0
        while right < n:

            total += nums[right]

            while total >= target:
                max_length = min(max_length, right-left+1)
                total -= nums[left]
                left += 1 
            right += 1 
        if max_length == float("inf"):
            return 0
        return max_length