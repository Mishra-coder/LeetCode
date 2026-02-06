class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1] + 1:
                start = nums[i]
            if i == len(nums) - 1 or nums[i] + 1 != nums[i+1]:
                res.append(str(start) if start == nums[i] else str(start) + "->" + str(nums[i]))
        return res
        