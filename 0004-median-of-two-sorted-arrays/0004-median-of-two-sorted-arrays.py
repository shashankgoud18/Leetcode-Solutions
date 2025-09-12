class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            result.append(nums2[j])
            j+= 1

        n = len(result)
        if n%2==1:
            final = result[n//2]
        else:
            mid1 = n//2 - 1
            mid2 = n//2
            final = (result[mid1] + result[mid2]) / 2

        return final