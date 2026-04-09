class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        final_set = set()
       
        max_length = 0
        while right<n:
            if s[right] not in final_set:
                final_set.add(s[right])
                max_length = max(max_length,right-left+1)
                right += 1 
            elif s[right] in final_set:
                final_set.remove(s[left])
                left += 1

        return max_length