class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        numSet = set(nums)
        for i in nums:
            if (i - 1) not in numSet:
                length =0
                while (i+length) in numSet:
                    length+=1
                
                count= max(length,count)
        return count

            