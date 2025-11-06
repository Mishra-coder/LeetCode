class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k>=n//2:        #infinite transaction
            total_profit = 0
            for i in range(1,n):
                if prices[i] > prices[i-1]:
                    total_profit += prices[i] - prices[i-1]
            return total_profit

        buy = [float("inf")] *(k+1)
        profit = [0] * (k+1)

        for price in prices:
            for t in range(1,k+1):
                buy[t] = min(buy[t],price-profit[t-1])
                profit[t] = max(profit[t],price-buy[t])
        return profit[k]





        