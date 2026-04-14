class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float('inf')
        for i in range(0,len(nums)):
            if nums[i] == target:
                ans = min(ans,abs(i-start))
        
        return ans