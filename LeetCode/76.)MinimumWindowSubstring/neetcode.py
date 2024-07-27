class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        h1, h2 = {}, {}

        for i in t:
            h1[i] = 1 + h1.get(i, 0)
        
        have = 0
        need = len(h1)

        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            h2[s[r]] = 1 + h2.get(s[r], 0)

            if s[r] in h1 and h2[s[r]] == h1[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                h2[s[l]] -= 1
                if s[l] in h1 and h2[s[l]] < h1[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res[0], res[1]
        
        return s[l:r + 1] if resLen != float("infinity") else ""

                