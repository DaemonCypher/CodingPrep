class Solution:
    def reverseBits(self, n: int) -> int:
        # convert n into binary
        value = bin(n)
        # remove the "0b" from the binary string
        txt = value.replace("0b","")
        # reverse the string
        txt = txt[::-1]
        # find the number of missing "0" at the end of string and add them
        # to the solution
        zeros=32-len(txt)
        txt = txt + ("0"*zeros)
        # convert the binary string back to int 
        return int(txt,2)