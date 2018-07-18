class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        first_part = nums[len(nums)-k:]
        second_part =nums[0:len(nums)-k]
        nums[:] =  first_part + second_part
        
        