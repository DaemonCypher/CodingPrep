class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for words in strs:
            size = len(words)
            res = res +str(size) +words + "~"
        return res


        # write your code here

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        res = []
        i = 0
        while i < len(str):
            size = 0
            while str[i].isdigit():
                size = size * 10 + int(str[i])
                i += 1
            i += 1  # Skip the word itself
            word = str[i:i+size]
            res.append(word)
            i += size + 1  # Skip the delimiter "~"
        return res