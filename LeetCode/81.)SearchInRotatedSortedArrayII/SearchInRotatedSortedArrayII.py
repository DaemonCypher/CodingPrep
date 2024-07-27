class Solution:
    def search(self, nums: List[int], target: int) -> bool:
            
        l = 0
        r = len(nums)-1
       
        
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            if nums[l] == nums[m]:
                l +=1
                continue
            # left portion
            if  nums[l] <= nums[m]:
                if target> nums[m] or target<nums[l]:
                    l = m +1
                else:
                    r = m -1
            # right portion
            else:
                if target< nums[m] or target> nums[r]:
                    r = m -1
                else:
                    l = m +1
            
        return False