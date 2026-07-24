class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = len(s)
        total = 0
        for i in range(n):
            if i<n-1 and hash_map[s[i]] < hash_map[s[i+1]]:
                total -= hash_map[s[i]]
            else:
                total += hash_map[s[i]]
        return total






