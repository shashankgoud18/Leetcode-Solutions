class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        result = 0

        right = len(s)-1
        while right >= 0:
            if s[right] == " " and result == 0:
                right -= 1
                continue
            elif s[right] == " ":
                return result
            else:
                result += 1
                right -= 1 
        
        return result
