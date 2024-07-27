class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp=nums2
        # make tmp be 1 long unsoted list
        for i in nums1:
            tmp.append(i)
        #sort tmp
        tmp.sort()
        length=len(tmp)

        index = float((length-1)/2)
        # if tmp is an odd length list 
        # makes it easy to find median
        if (length-1)%2==0:
            return float(tmp[int(index)])
        else:
            # if tmp is an even length list
            # get the left and right index from the median
            Rindex =index +0.5
            Lindex =index-0.5
            res = tmp[int(Rindex)]+tmp[int(Lindex)]
            res=res/2
            return res
        