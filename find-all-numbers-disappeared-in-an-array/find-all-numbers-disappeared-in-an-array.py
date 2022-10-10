class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_dic = {}
        res = []
        for i in nums:
            nums_dic[i] = 1
        
        for i in range(1,n+1):
            if i not in nums_dic:
                res.append(i)
        return res
    
# Time complexity O(n)
# Space complexity O(n)