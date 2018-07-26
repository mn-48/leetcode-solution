class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(int(num) for num in str(int("".join(str(num)  for num in digits))+1))
      