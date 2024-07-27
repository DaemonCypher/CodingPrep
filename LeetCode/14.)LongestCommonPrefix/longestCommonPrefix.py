class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        small = min(strs)
        itr = len(small)
        cur =0
        res =""
        while cur< itr:
            for word in strs:
                if small[cur] != word[cur]:
                    return res
            res= res+small[cur]

            cur +=1
        return res

        
