class Solution:
    def countBits(self, n: int) -> List[int]:
        res= [0]*(n+1)
        for i in range(len(res)):
            value = bin(i)
            res[i]= value.count("1")


        return res