class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        ans = -1
        l = 1
        r = x
        if x == 0:
            return 0
        while l<=r:
            mid = (l+r)//2
            if mid == x//mid:
                return mid
            elif mid > x//mid:
                r = mid - 1
            else:
                ans = mid 
                l = mid + 1 
        return ans
            
