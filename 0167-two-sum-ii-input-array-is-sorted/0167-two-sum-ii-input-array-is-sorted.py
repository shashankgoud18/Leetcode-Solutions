class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        hash_map = {}
        for i in range(1,n+1):
            check = target-numbers[i-1]
            if check in hash_map:
                return hash_map[check], i
            else:
                hash_map[numbers[i-1]] = i
            