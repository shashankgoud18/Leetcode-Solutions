class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        curr_sum = 0
        ans = 0
        hash_map = {0:1}

        for num in nums:
            curr_sum += num
            check = curr_sum-k
            if check in hash_map:
                ans += hash_map[check]
            hash_map[curr_sum] = hash_map.get(curr_sum,0)+1
        return ans