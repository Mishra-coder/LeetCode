class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        ans = 0
        for n in freq:
            if n + 1 in freq:
                ans = max(ans, freq[n] + freq[n + 1])
        
        return ans
        