class Solution:
    def hammingWeight(self, n: int) -> int:
        value =bin(n)
        count =0
        for i in value:
            if i == "1":
                count +=1
        return count