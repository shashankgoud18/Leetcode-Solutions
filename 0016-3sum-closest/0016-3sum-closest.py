class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')
        n = len(nums)
        for i in range(n):
            left = i+1
            right = n-1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if abs(currentSum-target) < abs(closestSum - target):
                    closestSum = currentSum
                
                if currentSum < target:
                    left += 1 
                elif currentSum > target:
                    right -= 1 
                else:
                    return currentSum
                

        
        return closestSum
                

