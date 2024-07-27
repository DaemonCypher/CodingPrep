class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using dictionary to store count of characters in string s
        sLetter = {}
        for i in s:
            if i in sLetter:
                sLetter[i] += 1
            else:
                sLetter[i] = 1

        # Checking if string t is anagram of string s
        for i in t:
            if i in sLetter:
                sLetter[i] -= 1
            else:
                return False

        # If any count is not zero, then they are not anagrams
        for value in sLetter.values():
            if value != 0:
                return False

        return True
