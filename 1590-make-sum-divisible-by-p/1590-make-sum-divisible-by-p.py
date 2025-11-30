class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        r = total % p
        if r == 0:   
            return 0

        last = {0: -1}   
        cur = 0
        ans = len(nums)

        for i, x in enumerate(nums):
            cur = (cur + x) % p
            target = (cur - r + p) % p

            if target in last:
                ans = min(ans, i - last[target])

            last[cur] = i

        return ans if ans < len(nums) else -1
        