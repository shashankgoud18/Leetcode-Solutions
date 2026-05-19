class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        hash_map = {}

        for word in strs:
            
            sorted_word = "".join(sorted(word))
            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
                continue
            hash_map[sorted_word] = [word]
        
        for key,val in hash_map.items():
            result.append(val)
        
        return result
