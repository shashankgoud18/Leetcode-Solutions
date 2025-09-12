class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        temp = []
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])
        m = len(temp)
        for i in range(m):
            nums[i] = temp[i]

        for i in range(m,n):
            nums[i] = 0
        return nums