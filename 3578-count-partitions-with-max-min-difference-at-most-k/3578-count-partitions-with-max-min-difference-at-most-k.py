class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0]*(n+1)
        pref = [0]*(n+1)
        dp[0] = pref[0] = 1

        maxdq = deque()
        mindq = deque()
        l = 0

        for r in range(n):
            v = nums[r]
            while maxdq and nums[maxdq[-1]] <= v:
                maxdq.pop()
            maxdq.append(r)
            while mindq and nums[mindq[-1]] >= v:
                mindq.pop()
            mindq.append(r)

            while nums[maxdq[0]] - nums[mindq[0]] > k:
                if maxdq[0] == l: maxdq.popleft()
                if mindq[0] == l: mindq.popleft()
                l += 1

            dp[r+1] = (pref[r] - (pref[l-1] if l > 0 else 0)) % MOD
            pref[r+1] = (pref[r] + dp[r+1]) % MOD

        return dp[n]
        