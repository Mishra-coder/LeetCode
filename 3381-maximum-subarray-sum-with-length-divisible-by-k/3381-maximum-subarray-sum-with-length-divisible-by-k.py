class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        p = 0
        mn = [10**30] * k
        mn[0] = 0
        ans = -10**30
        for i, x in enumerate(nums, 1):
            p += x
            r = i % k
            ans = max(ans, p - mn[r])
            mn[r] = min(mn[r], p)
        return ans
        