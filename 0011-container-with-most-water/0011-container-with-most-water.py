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
        h = float('inf') 
        result = 0
        while left<right:
            h = min(height[left],height[right])
            width = right - left 
            area = h*width
            result = max(area,result)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result