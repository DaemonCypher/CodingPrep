class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointer method
        l = 0   # left pointer
        r = len(numbers)-1  # right pointer

        while l<r:  
            # add the far right and left index of list
            cur = numbers[l] + numbers[r] 
            # since we know the list is ordered and the sum is too large
            # then we can move the right pointer more toward the middle
            if cur>target:
                r-=1
            # if the sum is too small we can move the left pointer towards the middle
            elif cur < target:
                l+=1
            # if the far left and right equals target
            else:
                return [l+1,r+1]
        # if nothing is found
        return []