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
        i = 0
        j = n-1
        min_height = float("inf")
        result = 0
        while i < j:
            min_height = min(height[i],height[j])
            width = j-i
            area = width * min_height
            result = max(area,result)

            if height[i] < height[j]:
                i += 1 
            else:
                j -= 1 
        return result



        