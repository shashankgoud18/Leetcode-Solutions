class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        curr_sum = 0
        prefix = {}
        for num in nums:
            curr_sum += num
            if curr_sum == k:
                count += 1
            
            if(curr_sum - k) in prefix:
                count += prefix[curr_sum - k]

            prefix[curr_sum] = prefix.get(curr_sum,0)+1
        return count
        