class NumArray:

    def __init__(self, nums: list[int]):
        n = len(nums)
        for i in range(1,n):
            nums[i] += nums[i-1]

        self.prefixSum = nums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        result = self.prefixSum[right] - self.prefixSum[left-1]
        return result



        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)