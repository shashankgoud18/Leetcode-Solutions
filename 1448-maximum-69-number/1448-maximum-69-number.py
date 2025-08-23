class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        final = 0
        flag = True
        for i in str(num):
            if i == '6' and flag:
                final = final*10 + int(9)
                flag = False
            else:
                final = final*10 + int(i)
        return final 
        