class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n-2):
            
            if i != 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = n-1

            while j<k:
                Sum = nums[i] + nums[j] + nums[k]
                if Sum == 0:
                    temp = [nums[i],nums[j],nums[k]]
                    result.append(temp)
                    j += 1 
                    k -= 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1 
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
                elif Sum < 0 :
                    j += 1
                elif Sum > 0:
                    k -= 1 
                
               
        return result