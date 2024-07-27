class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            p1,p2 = 0, 0
            for i in nums:
                
                temp = max(i +p1,p2)
                p1 = p2
                p2 =temp 
            return p2
        return max(helper(nums[1:]),helper(nums[:-1]),nums[0])
