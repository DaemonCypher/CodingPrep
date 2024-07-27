class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #create an empty set
        duplicate = set()
        # itterate through the list of numbers
        for i in nums:
            # grab the previous set length
            prev = len(duplicate)
            tmp = [i]
            # updates the set of numbers
            duplicate.update(tmp)
            # if the set already contains the newly add number than the length of set will
            # match the length pre-update set. Which means we found a duplicate, otherwise 
            # we keep iterating through the list of numbers
            if len(duplicate) == prev:
                return True

        return False
 
            