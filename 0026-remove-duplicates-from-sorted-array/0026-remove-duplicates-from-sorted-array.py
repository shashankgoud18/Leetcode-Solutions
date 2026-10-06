class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # n = len(nums)
        # freq_map = {}
        # for i in range(n):
        #     if nums[i] in freq_map:
        #         freq_map[nums[i]] += 1
        #     else:
        #         freq_map[nums[i]] = 1
        
        # freq_map = sorted(freq_map)
        # j = 0
        # for k in freq_map:
        #    nums[j] = k
        #    j += 1
        
        # return j

        i = 1
        for j in range(1,len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        return i
       