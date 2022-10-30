class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = ((x>0)-(x<0))*int(str(abs(x))[::-1])
        return 0 if ans < -2 ** 31 or ans >= 2 ** 31 else ans