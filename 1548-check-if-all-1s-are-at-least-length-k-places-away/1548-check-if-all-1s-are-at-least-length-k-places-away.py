class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        last = -1
        for i in range(n):
            if nums[i] == 1:
                if last != -1 and (i-last-1) < k:
                    return False
                last = i
                
        return True