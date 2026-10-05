class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # j = 0
        # for i in range(m,m+n):
        #     nums1[i] = nums2[j]
        #     j += 1
        # result = sorted(nums1)
        # return result
        # p1 = m-1
        # p2 = n-1
        # p = m+n-1
        # while p1>=0 and p2>=0:
        #     if nums1[p1] > nums2[p2]:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
        #     else:
        #         nums1[p] = nums2[p2]
        #         p2-=1
        #     p-=1
        # while p2>=0:
        #     nums1[p] = nums2[p2]
        #     p2-=1
        #     p-=1
        
        # return nums1

        r1 = m-1
        r2 = n-1
        w = m+n-1

        while r2>=0:
            if r1 >= 0 and nums1[r1] > nums2[r2]:
                nums1[w] = nums1[r1]
                r1 -=1 
            else:
                
                nums1[w] = nums2[r2]
                r2 -= 1
            w -= 1 
