class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        #Brute Forcce
        # n = len(nums)
        # max_subarr = 0
        # for i in range(n):
        #     zeros = 0
        #     for j in range(i,n):
        #         if nums[j]== 0:
        #             zeros += 1 
        #         if zeros>1:
        #             break
        #         max_subarr = max(max_subarr,j-i)
                
                
        # return max_subarr

        left = 0
        right = 0
        n = len(nums)
        zeros = 0
        max_subarr = 0
        while right<n:
            if nums[right] == 0:
                zeros += 1
            while zeros>1:
                if nums[left] == 0:
                    zeros -= 1 
                left += 1
            
            max_subarr = max(max_subarr,right-left)
            right += 1
        
        return max_subarr
            


