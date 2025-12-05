class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        n = len(nums)
        return (n - 1) if total % 2 == 0 else 0