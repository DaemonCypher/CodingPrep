class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x< 0:
            neg = True
            x=x*-1
        val = str(x)
        val =val[::-1]
        val =int(val)
        if val > 2147483647 or val < -2147483648:
            return 0
        if neg:
            val = val*-1
        return val
        