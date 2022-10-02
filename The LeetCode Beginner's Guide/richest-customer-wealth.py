# Time complexity O(nxm)
# Space complexity O(1)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = 0
        for i in accounts:
            mx = max(sum(i), mx)
        return mx
           
            
