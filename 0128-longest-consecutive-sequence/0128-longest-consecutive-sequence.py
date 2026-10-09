class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        s = set(nums)
        max_count = 0
        for num in nums:
            count = 1
            if num-1 not in s:
                while num+1 in s:
                    num = num+1
                    count += 1

            
            max_count = max(count,max_count)
        return max_count
            

