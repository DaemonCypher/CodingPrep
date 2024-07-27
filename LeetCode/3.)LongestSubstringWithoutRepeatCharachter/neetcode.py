class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp=set()
        #left index
        leftI=0
        count=0
        #rightI = right index
        for rightI in range(len(s)):
            while s[rightI] in tmp:
                tmp.remove(s[leftI])
                leftI+=1
            tmp.add(s[rightI])
            count=max(count,rightI-leftI+1)
        return count
