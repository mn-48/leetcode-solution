import re
import math
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        mx = 2**31 
        mn = int(-2**31)
        
        n = re.match('\s*[-+]?\d+',str)
        num = 0
        if n:
            num = int(n.group())
        if num >=mx:
            num = mx-1
        if num <= mn:
            num = mn
        return num
        