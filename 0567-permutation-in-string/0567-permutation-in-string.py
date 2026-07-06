class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        n = len(s1)
        h1 = {}
        for ch in s1:
            h1[ch] = h1.get(ch,0)+1
        
        h2 = {}
        for i in range(n):
            h2[s2[i]] = h2.get(s2[i],0)+1

        if h1 == h2:
            return True
        
        l = 0
        r = n
        m = len(s2)
        while r<m:
            h2[s2[r]] = h2.get(s2[r],0)+1

            h2[s2[l]] -= 1
            if h2[s2[l]] == 0:
                del h2[s2[l]]
            l+=1

            r += 1
            if h1 == h2:
                return True
        
        return False
