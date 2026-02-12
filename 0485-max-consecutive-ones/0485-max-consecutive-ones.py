class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        curr = 0
        
        for num in nums:
            if num == 1:
                curr += 1
                max_count = max(max_count, curr)
            else:
                curr = 0
        
        return max_count
        