class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums = sorted(nums)
        length = len(nums)
        if length % 2:
            n = nums[length // 2]
            return n
        else:
            n = (nums[length // 2] + nums[(length // 2) - 1]) / 2
            return n
'''
obj = Solution()
print(obj.findMedianSortedArrays([1, 2],[3,4]))

'''



