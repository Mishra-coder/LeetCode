class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        first_buy = float("inf")
        first_profit = 0
        sec_buy = float("inf")
        sec_profit = 0

        for price in prices:
            first_buy = min(first_buy,price)
            first_profit = max(first_profit,price-first_buy)
            sec_buy = min(sec_buy,price-first_profit)
            sec_profit =  max(sec_profit,price-sec_buy)
        return sec_profit

        