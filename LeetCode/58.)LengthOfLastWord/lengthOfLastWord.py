class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        res=[]
        for i in range(len(s)):
            if s[i] == " ":
                res.append(length)
                length=0
            else:
                length+=1
        res.append(length)
        for i in range(len(res)-1,-1,-1):
            if res[i] > 0:
                return res[i]
 