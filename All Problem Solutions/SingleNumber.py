class Solution:
    def singleNumber(self, nums):
        new_list = []
        for i in nums:
            if i in new_list:
                new_list.remove(i)
            else:
                new_list.append(i)
        return new_list.pop()