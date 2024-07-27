class Solution:
    def rob(self, nums: List[int]) -> int:
        p1,p2 = 0, 0
        for i in nums:
            
            temp = max(i +p1,p2)
            p1 = p2
            p2 =temp 
        return p2

  
