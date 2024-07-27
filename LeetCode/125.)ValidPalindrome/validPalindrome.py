class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert string to lower
        s = s.casefold()
        # mask
        alphaNumeric = "qwertyuiopasdfghjklzxcvbnm1234567890"
        # res equals s for the edge case where the for loop does not
        # remove any chars from s
        res = s
        for char in s:
            if char not in alphaNumeric:
                res = s.replace(char,"")
                s = res
        # reverse the string and compare if both are equal for palindrome
        left = res
        right = res[::-1]

        if left == right:
            return True
        else:
            return False