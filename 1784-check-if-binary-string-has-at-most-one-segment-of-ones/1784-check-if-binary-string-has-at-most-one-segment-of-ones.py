class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        seen_zero = False

        for ch in s:
            if ch == '0':
                seen_zero = True
            if seen_zero and ch == '1':
                return False
        
        return True
