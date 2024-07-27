class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        for k,v in res.items():
            if v ==1:
                return k