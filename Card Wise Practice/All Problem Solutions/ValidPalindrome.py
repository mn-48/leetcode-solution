class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = [ch.lower() for ch in s if ch.isalnum()]
        #make a list which contains only alpha-numeric char
        return st[:]==st[::-1] 
        #compare the char that is Valid Palindrome or not
