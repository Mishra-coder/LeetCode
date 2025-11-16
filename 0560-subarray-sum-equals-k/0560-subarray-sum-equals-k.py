class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mp = {0: 1}
        s = 0
        ans = 0
        for x in nums:
            s += x
            ans += mp.get(s - k, 0)
            mp[s] = mp.get(s, 0) + 1
        return ans
        