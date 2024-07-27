class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        value = nums.count(val)

        for i in range(value):
            nums.remove(val)
        return len(nums)