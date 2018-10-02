class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483647:
            x = 0
            return x
        if x < -2147483647:
            x = 0
            return x
        if x == 0:
            return x
        if x >0:
            while x < 2147483648:
                x = str(x)
                x = x[::-1]
                x = x.lstrip("0")
                x = int(x)
                if x <= 2147483647:
                    return x
                else:
                    x = 0
                    return x
        if x < 0:
            while x > -2147483647:
                x = str(x)
                x = x.replace ('-', '')
                x = x[::-1]
                x = x.lstrip("0")
                x = '-' + x
                x = int(x)
                if x >= -2147483647:
                    return x
                else:
                    x = 0
                    return x
                
                return x
