class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        n = len(s)
        final = set()
        max_subarr = 0
        while right<n:

            while s[right] in final:
                final.remove(s[left])
                left += 1 
            
            final.add(s[right])
            max_subarr = max(max_subarr,right-left+1)
            right += 1

        return max_subarr
                

    


