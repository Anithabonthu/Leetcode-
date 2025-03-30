class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res=[0]*(m+n)
        k=0
        i,j=0,0
        while i < m and j <n:
            if nums1[i]<=nums2[j]:
                res[k]=nums1[i]
                i+=1
            else:
                nums2[j]<nums1[i]
                res[k]=nums2[j]
                j+=1
            k+=1
        while i<m:
            res[k]=nums1[i]
            i+=1
            k+=1
        while j <n:
            res[k]=nums2[j]
            j+=1
            k+=1
        for r in range((m+n)):
            nums1[r]=res[r]
            