class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        formed = 0
        t_map = {}
        window = {}
        ans = (inf, 0, 0)
        for ch in t:
            t_map[ch] = t_map.get(ch,0)+1 
        required = len(t_map)

        while right < len(s):
            ch = s[right]
            window[ch] = window.get(ch,0)+1 
            if ch in t_map:
                if t_map[ch] == window[ch]:
                    formed += 1
            
            
            while formed == required:
                current_window_length = right - left+1
                if current_window_length < ans[0]:
                    ans = (current_window_length, left, right)
                window[s[left]] -= 1
                if s[left] in t_map and window[s[left]] < t_map[s[left]]:
                   formed -= 1
                left += 1
            
            right += 1
        
        if ans[0] == inf:
             return ""
        return s[ans[1]:ans[2]+1]
