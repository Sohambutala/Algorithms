class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = m-1, n-1
        index = m+n-1
        while index>=0:
            if j<0:
                break
            if i>=0 and nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i-=1
            else:
                nums1[index] = nums2[j]
                j-=1
            index -=1