
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)
        
    #--------------------------
        return reduce(lambda x, y: x ^ y, nums)
    #--------------------------
        # res = 0
        # for num in nums:
        #     res ^= num
        # return res
    #--------------------------
        # c = Counter(nums)
        # print(c)
        
        # set_nums = set(nums)
        # for i in set_nums:
        #     if c[i] == 1:
        #         return i
                
        