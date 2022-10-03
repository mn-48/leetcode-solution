class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        currSum = mxSum = nums[0]
        for i in nums[1:]:
            currSum = max(i, currSum+i)
            mxSum = max(currSum, mxSum)
        return mxSum
        