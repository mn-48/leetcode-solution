# Time complexity O(lon(n))
# Space complexity O(1)

class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num:
            if num&1:
                num -=1
            else:
                # num = num >> 1
                num = num //2
            cnt+=1
        return cnt
        
