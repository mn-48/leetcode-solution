class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums[:]= sorted(set(nums), reverse=True)
        # print(nums)
        n = len(nums)
        if n<3:
            return max(nums, default=nums[0])
        return nums[2]