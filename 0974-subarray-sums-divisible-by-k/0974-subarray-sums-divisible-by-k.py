class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        freq = {0:1}
        n = len(nums)
        prefix_sum = 0
        count = 0
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum%k in freq:
                count += freq[prefix_sum%k]
                freq[prefix_sum%k] += 1
            else:
                freq[prefix_sum%k] = freq.get(prefix_sum%k,0)+1
        
        return count