class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        profit = 0
        max_onwards = [0] * n
        
        for i in range(n - 2, -1, -1):
            max_onwards[i] = max(max_onwards[i + 1], prices[i + 1])
            
        for i in range(n):
            max_onwards[i] = max_onwards[i] - prices[i]
            
        for i in range(n):
            profit = max(profit, max_onwards[i])
            
        return profit