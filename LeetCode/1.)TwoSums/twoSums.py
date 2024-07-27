class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force method of trying every possible combination from left to right.

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # check if i and (i+1),(i+2),... equals the target
                if nums[j] == target - nums[i]:
                    return [i, j]