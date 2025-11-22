class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops = 0
        for x in nums:
            if x % 3 != 0:
                ops += 1
        return ops
        