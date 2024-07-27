class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # add everything from nums2 to the end of nums1
        for j in range(n):
            nums1[m+j] = nums2[j]

        # use python built in sort function to sort it
        nums1.sort()