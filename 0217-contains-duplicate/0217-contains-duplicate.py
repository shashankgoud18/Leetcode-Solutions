class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash_map = {}
        # for ch in nums:
        #     if ch in hash_map:
        #         return True
        #     hash_map[ch] = 1
        
        # return False

        s = set()
        for ch in nums:
            if ch in s:
                return True
            s.add(ch)
        
        return False