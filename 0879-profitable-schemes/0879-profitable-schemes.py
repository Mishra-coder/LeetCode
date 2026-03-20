class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7

        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for g, p in zip(group, profit):
            for members in range(n, g - 1, -1):
                for prof in range(minProfit, -1, -1):
                    new_profit = min(minProfit, prof + p)
                    dp[members][new_profit] = (
                        dp[members][new_profit] +
                        dp[members - g][prof]
                    ) % MOD
        
        return sum(dp[m][minProfit] for m in range(n + 1)) % MOD