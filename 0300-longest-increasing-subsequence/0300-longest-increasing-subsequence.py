class Solution:
    def lengthOfLIS(self, num):
        n = len(num)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if num[i] > num[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
