class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, float('-inf'), float('-inf')]

        for x in nums:
            r = x % 3
            dp_old = dp[:]  
            for j in range(3):
                new_r = (j + r) % 3
                dp[new_r] = max(dp[new_r], dp_old[j] + x)

        return dp[0]