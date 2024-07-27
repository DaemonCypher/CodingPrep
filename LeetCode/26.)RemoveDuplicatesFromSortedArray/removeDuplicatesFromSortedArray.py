class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = -1000
        for i in range(len(nums)):
            if nums[i] !=check:
                check = nums[i]    
            else:
                nums[i] = 101
        nums.sort()
        value = len(nums) - nums.count(101)
    
        return value

