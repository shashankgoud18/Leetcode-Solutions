class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute Force
        # n = len(nums)
        # ans = float('-inf')
        # for i in range(n):
        #     product = 1 
        #     for j in range(i,n):
        #         product *= nums[j]
        #         ans = max(ans,product)
        
        # return ans

        #Optimal DP
        n = len(nums)
        minEnding = nums[0]
        maxEnding = nums[0]
        ans = nums[0]

        for i in range(1,n):
            prevMax = maxEnding
            prevMin = minEnding

            maxEnding = max(nums[i], prevMax*nums[i],prevMin*nums[i])
            minEnding = min(nums[i],prevMin*nums[i],prevMax*nums[i])

            ans = max(ans,max(maxEnding,minEnding))
        
        return ans

        #Optimal
        left = 0
        right = n-1 
        prefixPro = 1 
        suffixPro = 1 
        ans = nums[0]
        while left<=right:
            
            prefixPro *= nums[left]
            suffixPro *= nums[right]

            ans = max(prefixPro,suffixPro)
            left += 1 
            right -= 1 
        
        return ans

