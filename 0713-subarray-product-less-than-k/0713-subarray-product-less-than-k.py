class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        
        #Brute Force
        # count = 0 

        # for i in range(len(nums)):
        #     product = 1 
        #     for j in range(i,len(nums)):
        #         product *= nums[j]
        #         if product < k:
        #             count += 1
            
        # return count

        # optimal
        if k <= 1:
            return 0
        count = 0
        left = 0
        right = 0
        n = len(nums)
        product = 1
        while right<n:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1           
            right +=1 
        return count
