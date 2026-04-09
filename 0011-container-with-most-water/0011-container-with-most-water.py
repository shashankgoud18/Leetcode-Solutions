class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Brute Force
        # n = len(height)
        # result = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         area = (j-i) * min(height[i],height[j])
        #         result = max(result,area)
        
        # return result
        n = len(height)
        left = 0
        right = n-1
        result = 0
        while left<right:
            dis = right - left 
            area = dis*min(height[left],height[right])
            result = max(result,area)

            if height[left]<=height[right]:
                left += 1 
            else:
                right -= 1 
        
        return result
        
            