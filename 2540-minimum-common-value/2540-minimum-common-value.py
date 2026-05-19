class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # common = float("inf")
        # n = len(nums1)
        # m = len(nums2)
        # for i in range(n):
        #     for j in range(m):
        #         if nums1[i] == nums2[j]:
        #             common = min(common,nums1[i])

        # if common == float("inf"):
        #     return -1
        # return common


        common = float("inf")
        left = 0
        right = 0
    

        while left<len(nums1) and right<len(nums2):
            if nums1[left] == nums2[right]:
                print(nums1[left])
                common = min(common,nums1[left])
                left += 1 
                right += 1 
                continue
            elif nums1[left] < nums2[right]:
                left += 1 
                continue
            else:
                right += 1 
                continue
            
            
        
        if common == float("inf"):
            return -1
        return common
