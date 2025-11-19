class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        n = len(nums)
        for i in range(n):
            if original in nums:
                original = original*2
        return original