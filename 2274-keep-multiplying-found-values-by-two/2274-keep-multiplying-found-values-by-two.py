class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums = set(nums)
        while True:
            if original in nums:
                original *= 2
            else:
                break

        return original
        