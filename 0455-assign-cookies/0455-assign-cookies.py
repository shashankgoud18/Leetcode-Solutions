class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left = 0
        right = 0
        n = len(s)
        m = len(g)
        g = sorted(g)
        s = sorted(s)
        maxi = 0
        while right < n and left < m:
            if g[left] <= s[right]:
                maxi += 1
                left += 1
                right += 1
            else: 
                right += 1
        return maxi
            