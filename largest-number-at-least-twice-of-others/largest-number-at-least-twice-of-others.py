class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx1 = 0
        mx2 = 0
        for n in nums:
            if n > mx1:
                mx2 = mx1
                mx1 = n
            elif n > mx2:
                mx2 = n
        if mx1 >= 2*mx2:
            return nums.index(mx1)
        return -1
        
             
# Time complexity O(n)
# Space complexity O(1)