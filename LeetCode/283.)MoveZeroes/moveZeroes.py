class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find how many 0 there are in the list
        count = nums.count(0)

        # remove the 0s and add them to the end
        for i in range(count):
            nums.remove(0)
        for i in range(count):
            nums.append(0)