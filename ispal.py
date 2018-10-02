class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            x = bool(1)
            return x
        else:
            x = bool(0)
            return x
        """
        :type x: int
        :rtype: bool
        """
