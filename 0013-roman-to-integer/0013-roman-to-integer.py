class Solution:
    def romanToInt(self, s: str) -> int:

        # num = 0
        # for ch in s:
        #     if ch == "I":
        #         num += 1 
        #     if ch == "V":
        #         num += 5 
        #     elif ch == "X":
        #         num += 10
        #     elif ch == "L":
        #         num += 50
        #     elif ch == "C":
        #         num += 100
        #     elif ch == "D":
        #         num += 500
        #     elif ch == "M":
        #         num += 1000
        # return num

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






