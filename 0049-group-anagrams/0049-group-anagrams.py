class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        hmap = {}

        for ch in strs:
            sorted_ch = "".join(sorted(ch))
            
            if sorted_ch in hmap:
                hmap[sorted_ch].append(ch)
            else:
                hmap[sorted_ch] = [ch]
            
        
        for key,val in hmap.items():
            result.append(val)
        
        return result
