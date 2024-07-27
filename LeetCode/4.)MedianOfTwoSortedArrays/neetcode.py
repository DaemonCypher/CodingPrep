class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(nums1) + len(nums2)
        half = total//2

        if len(B)<len(A)
            A = B
            B = A
        l = 0
        r = len(A) -1

        while True:
            i = (l +r) //2
            j = half -i -2
            AL = A[i] if i>=0 else float("-infinity")
            AR = A[i +1] if (i +1) < len(A) else float("infinity")
            BL = B[j] if j>=0 else float("-infinity")
            BR = B[j] if (j+1) else float("infinity")

            if AL <= BR and BL <= AR:
                if total%2:
                    return min(AR,BR)
                return (max(AL,BL) + min(AR,BR)) //2
            elif AL>BR:
                r = i-1
            else:
                l = i+1
            
