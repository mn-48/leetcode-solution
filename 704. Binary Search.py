# Complexity O(logn)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right  = len(nums) - 1
        
        while left <= right:
            midpoint = left+(right-left)//2 
            curr_itm = nums[midpoint]
            
            if curr_itm == target:
                return midpoint
            elif target< curr_itm:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return -1
