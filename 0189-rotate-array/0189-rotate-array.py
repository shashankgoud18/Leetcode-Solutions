class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not eturn anything, modify nums in-place instead.
        """
        #Brute Force
        # ans = []
        # n = len(nums)
        # k %= n
        
        # for i in range(n):
        #     if i > n-k-1:
        #         ans.append(nums[i])  
        # start = n-k
        # for i in range(0,start):
        #     ans.append(nums[i])
        
        # nums[:] = ans

        #Optimal
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        
        