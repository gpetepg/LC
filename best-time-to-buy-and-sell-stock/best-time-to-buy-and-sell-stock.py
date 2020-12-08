class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_stock = float("inf")
        
        for i in range(1, len(prices)):
            curr_stock = min(curr_stock, prices[i], prices[i -1])
            profit = max(profit, (prices[i] - curr_stock))
            
        return profit
