class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_nums = []
        sm = 0
        for i in nums:
            sm +=i
            sum_nums.append(sm)
        return sum_nums
