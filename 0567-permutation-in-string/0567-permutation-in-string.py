class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        m = len(s2)
        s1_freq = {}
        s2_freq = {}
        if n > m:
            return False
        for i in range(n):
            s1_freq[s1[i]] = s1_freq.get(s1[i],0)+1
        
        i = 0
        j = 0

        while j < m:
            s2_freq[s2[j]] = s2_freq.get(s2[j],0)+1

            if j-i+1 > n:
                s2_freq[s2[i]] -= 1 
                if s2_freq[s2[i]] == 0:
                    del s2_freq[s2[i]]
                i += 1 

 
            if s1_freq == s2_freq:
                return True
            
            j += 1 
        return False