class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s =""
        for i in digits:
            s= s + str(i)
        s = int(s)
        s+=1
        s = str(s)
        res =[]
        for c in s:
            res.append(int(c))
        return res