class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_max = 0
        left = []
        for i in range(0,n):
            left_max = max(left_max,height[i])
            left.append(left_max)
        
        right_max = 0
        right = [0]*n
        for i in range(n-1,-1,-1):
            right_max = max(right_max,height[i])
            right[i] = right_max
        
        water = 0
        for i in range(0,n):
            water += min(left[i],right[i]) - height[i]
        return water