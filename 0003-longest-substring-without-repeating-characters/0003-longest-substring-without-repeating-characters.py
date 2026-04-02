class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        max_length = 0
        char_set = set()
        while r<len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1 
            char_set.add(s[r])
            max_length = max(max_length, r-l+1)
            r += 1
        return max_length