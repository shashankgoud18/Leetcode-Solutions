class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign = -1
            x = -x
        else:
            sign = 1
        
        result = 0
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        while x > 0:
            last_digit = x % 10      
            x = x//10
            if (result > INT_MAX // 10) or \
               (result == INT_MAX // 10 and last_digit > (7 if sign == 1 else 8)):
               return 0
            result = result*10 + last_digit

        return result*sign

        