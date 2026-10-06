class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}

        for ch in magazine:
            map[ch] = map.get(ch,0)+1
        
        for ch in ransomNote:
            if ch in map:
                if map[ch] == 0:
                    return False
                map[ch] -= 1
            else:
                return False
        return True