class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_s = ''
        for ch in s:
            if ch.isalnum():
                final_s += ch.lower()
        
        return final_s == final_s[::-1]