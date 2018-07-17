class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
     
        return len(list(set(nums)))
        """
        indx = 0
        
        for i in range(1, len(nums)):
            if nums[indx] != nums[indx+1]:
                indx += 1
            else:
                del nums[indx]
        
        return len(nums)
        