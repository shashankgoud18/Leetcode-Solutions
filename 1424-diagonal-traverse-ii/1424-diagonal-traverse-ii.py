class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        freq = {}
        m = len(nums)

        for i in range(m):
            n = len(nums[i])
            for j in range(n):
                index = i+j
                if index in freq:
                    freq[index].append(nums[i][j])
                else:
                    freq[index] = [nums[i][j]]
        
        result = []

        for key,val in freq.items():
            result.extend(val[::-1])
        
        return result