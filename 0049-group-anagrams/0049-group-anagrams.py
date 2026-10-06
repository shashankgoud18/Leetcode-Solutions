class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        hashmap = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)
            else:
                hashmap[sorted_word] = [word]
       

        for key,val in hashmap.items():
            result.append(val)
        return result