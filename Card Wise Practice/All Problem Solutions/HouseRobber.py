class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous, current = 0 , 0
        for n in nums:
            previous, current = current, max(previous + n, current)
        return current;
            