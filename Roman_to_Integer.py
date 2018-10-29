class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        dicts = {'I':1,
                'V':5,
                'X':10, 
                'L':50, 
                'C':100,
                'D':500, 
                'M':1000,
                'IV':-2, 
                'IX':-2, 
                'XL':-20,  
                'XC':-20,
                'CD':-200,
                'CM':-200}
        for key in dicts:
            num = num + s.count(key)*dicts[key]
        return num
