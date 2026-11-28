class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}

        for ch in arr:
            freq[ch] = freq.get(ch,0)+1
        
        s = set()

        for value in freq.values():
            if value in s:
                return False
            s.add(value)
        
        return True