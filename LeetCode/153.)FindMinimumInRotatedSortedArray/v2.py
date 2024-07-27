class Solution:
    def findMin(self, nums: List[int]) -> int:
        # assign smallest to some value in nums
        smallest = max(nums)
        left =0
        right = len(nums)-1
        # check the left and right side of nums and find the smallest 
        # between the two or the current smallest
        while left<=right:
            smallest = min(smallest,nums[left],nums[right])
            left +=1
            right-=1
        return smallest