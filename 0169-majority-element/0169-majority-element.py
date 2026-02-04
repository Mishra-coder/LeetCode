class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1

        return candidate
        