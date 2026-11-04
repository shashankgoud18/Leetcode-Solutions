class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # n = len(s)
        # k = len(p)

        # freqp = {}
        # window = {}
        # res = []

        # if k>n:
        #     return res

        # for ch in p:
        #     freqp[ch] = freqp.get(ch,0)+1 
        
        # for i in range(k):
        #     ch = s[i]
        #     window[ch] = window.get(ch,0)+1
        #     print(window)
        
        # if freqp == window:
        #     res.append(0)
        
        # for i in range(k,n):
        #     window[s[i]] = window.get(s[i],0)+1
        #     remove_char = s[i-k]
        #     window[remove_char] -= 1 

        #     if window[remove_char] == 0:
        #         del window[remove_char]

        #     if window == freqp:
        #         res.append(i-k+1)
        # return res


        n = len(s)
        m  = len(p)

        s_freq = {}
        p_freq = {}

        for i in range(m):
            p_freq[p[i]] = p_freq.get(p[i],0)+1

        i = 0
        j = 0
        result = []

        while j < n:
            ch = s[j]
            s_freq[ch] = s_freq.get(ch,0)+1

            if j-i+1 > m:
                s_freq[s[i]] -= 1 
                if s_freq[s[i]] == 0:
                    del s_freq[s[i]]
                i += 1

            
            if s_freq == p_freq:
                result.append(i)
            j += 1

        return result














