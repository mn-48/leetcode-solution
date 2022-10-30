class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_max, final_max = 0, 0
        for i in range(1, len(prices)):
            current_max += prices[i] - prices[i-1]
            current_max = max(0,current_max )
            final_max =max(current_max, final_max)
            
        return final_max
        