class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        profit = 0
        
        for i in range(len(prices) - 1):
            buy = min(buy, prices[i], prices[i + 1])
            
            profit = max((prices[i + 1] - buy), profit)              
        
        return profit
