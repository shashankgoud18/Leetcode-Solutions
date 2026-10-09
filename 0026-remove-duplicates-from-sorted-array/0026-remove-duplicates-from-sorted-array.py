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

        slow = 0
        count = 0
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1 
                nums[slow] = nums[fast]
                count += 1
            
        return count+1