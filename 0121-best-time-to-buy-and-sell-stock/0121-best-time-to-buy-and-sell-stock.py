class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        profit=0
        for i in range(len(prices)):
            buy=min(buy,prices[i])
            profit=max(profit,prices[i]-buy)
        return profit
        