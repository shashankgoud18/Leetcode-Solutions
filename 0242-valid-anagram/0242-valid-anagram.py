class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # freq = [0]*26
        # for i in range(len(s)):
        #     freq[ord(s[i]) - ord('a')] += 1
        #     freq[ord(t[i]) - ord('a')] -= 1 
        
        # for i in range(len(freq)):
        #     if freq[i] != 0:
        #         return False
        
        # return True
        hmap1 = {}
        hmap2 = {}

        for i in range(len(s)):
            ch = s[i]
            ch2 = t[i]
            hmap1[ch] = hmap1.get(ch,0)+1
            hmap2[ch2] = hmap2.get(ch2,0)+1
        
        return hmap1 == hmap2
