class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        started = False
        for ch in s:
            if ch == " " and not started:
                continue
            if ch == "-" and not started:
                sign = -1
                started = True
                continue
            elif ch == "+" and not started:
                sign = 1
                started = True
                continue
            
            if ch.isdigit():
                result = result*10 + int(ch)
                started = True
            else:
               break
        
        result = sign*result
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result