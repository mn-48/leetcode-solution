class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        
        for i, x in enumerate(nums):
            if left_sum == S-left_sum-x:
                return i
            
            left_sum += x
        return -1
    
# Time complexity O(n)
# Space complexity O(n)