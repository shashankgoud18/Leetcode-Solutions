class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not eturn anything, modify nums in-place instead.
        """
        ans = []
        n = len(nums)
        k %= n
        
        for i in range(n):
            if i > n-k-1:
                ans.append(nums[i])
                
        
        start = n-k

        for i in range(0,start):
            ans.append(nums[i])
        
        nums[:] = ans